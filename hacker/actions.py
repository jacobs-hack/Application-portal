import unicodecsv
import openpyxl
from openpyxl import styles
from openpyxl.cell import cell
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse


def get_direct_prop(obj, fields):
    """ Gets a model property of an object """

    # shouldn't happen, but whatever
    if len(fields) == 0:
        return obj

    # if we have a single field to get
    elif len(fields) == 1:
        field = fields[0]

        # we may have a display getter
        try:
            display_getter = 'get_{}_display'.format(field)
            if hasattr(obj, display_getter):
                return getattr(obj, display_getter)()
        except:
            pass

        #if we do not, return the field itself
        return getattr(obj, field)

    # else go recursively
    else:
        return get_direct_prop(getattr(obj, fields[0]), fields[1:])


def get_model_prop(modeladmin, obj, field, default=None):
    """ Gets a model property or None"""
    try:
        try:
            return get_direct_prop(obj, field.split("__"))
        except AttributeError:
            try:
                attr = getattr(modeladmin, field)
                return attr(obj)
            except AttributeError:
                return default
    except ObjectDoesNotExist:
        return default

def to_excel(value):
    """ Turns any value into a value understood by excel """

    # if we know the type, return it immediatly
    if isinstance(value, cell.KNOWN_TYPES):
        return value

    # if we are none of the above and have a name, return the name
    elif hasattr(value, "name"):
        return to_excel(getattr(value, "name"))

    # if we are a list, return the list
    elif isinstance(value, list):
        return ', '.join(map(to_excel, value))

    # fallback to string
    else:
        return str(value)


def export_as_xslx_action(description="Export selected objects as XSLX file",
                          fields=None, header=True):
    """
    Return an action that exports the given fields as XSLX files
    """

    def export_as_xslx(modeladmin, request, queryset):

        # get fields to export
        opts = modeladmin.model._meta
        if not fields:
            field_names = [field.name for field in opts.fields]
        else:
            field_names = fields

        # Create a response header
        response = HttpResponse(
            content_type='application/application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename={}.xlsx'.format(str(opts).replace('.', '_'))

        # Create a new workbook
        wb = openpyxl.Workbook()
        wb_row = 0
        ws = wb.get_active_sheet()
        ws.title = str(opts).replace('.', '_')


        # Write the header (if desired)
        if header:
            for i, field in enumerate(field_names):
                c = ws.cell(row=wb_row + 1, column=i + 1)
                c.value = field
                c.font = styles.Font(bold=True)
            wb_row += 1

        # Write each of the rows
        for obj in queryset:
            for i, field in enumerate(field_names):
                c = ws.cell(row=wb_row + 1, column=i + 1)

                # Get the excel value and store it into the field
                prop = get_model_prop(modeladmin, obj, field)
                try:
                    c.value = to_excel(prop)
                except:
                    c.value = str(prop)
            wb_row += 1

        # adjust column widths
        # adapted from https://stackoverflow.com/a/39530676
        for col in ws.columns:
            max_length = 0
            column = col[0].column  # Get the column name
            for cell in col:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(cell.value)
                except:
                    pass
            adjusted_width = (max_length + 2) * 1.2
            ws.column_dimensions[column].width = adjusted_width

        # and export
        wb.save(response)
        return response

    export_as_xslx.short_description = description
    return export_as_xslx
