from django.contrib import admin

from hacker.actions import export_as_xslx_action
from .models import Hacker, HackathonApplication, \
    AcademicData, Approval, Skills


class HackerApprovalInline(admin.StackedInline):
    model = Approval


class HackerAcademicDataInline(admin.StackedInline):
    model = AcademicData


class HackerHackathonApplicationInline(admin.StackedInline):
    model = HackathonApplication


# TODO: This
class SkillsInline(admin.StackedInline):
    model = Skills


class SetupCompleted(admin.SimpleListFilter):
    title = 'Setup Status'
    parameter_name = 'completed'
    
    def lookups(self, request, modeladmin):
        return [
            ('1', 'Completed'), 
            ('0', 'Incomplete')
        ]
    
    def queryset(self, request, queryset):
        if self.value() == '1':
            # TODO: Use last field
            return queryset.filter(skills__isnull=False)
        elif self.value() == '0':
            # TODO: Use last field
            return queryset.filter(skills__isnull=True)
        else:
            return queryset


class HackerAdmin(admin.ModelAdmin):
    inlines = [
        HackerApprovalInline,
        HackerAcademicDataInline,
        HackerHackathonApplicationInline,
        SkillsInline
    ]

    # Fields that should be searchable
    # TODO: We probably want the university (once we have that field)
    search_fields = [
        'firstName', 'middleName', 'lastName', 'email',
    ]

    # Fields that are displayed in the admin view
    # TODO: We want to clean up the basic fields to be shown here
    list_display = (
        # basic information
        'fullName', 'email', 'userApproval', 'completedSetup',

    )

    # Fields that can be dynamically filtered for
    # TODO: We want to have all sorts of fields here
    list_filter = (
        'approval__approval', SetupCompleted,
    )

    # List of all fields, for the xslx export
    # TODO: Do this properly
    full_export_fields = (
        # Profile data
        'profile__username', 'profile__is_staff', 'profile__is_superuser',
        'profile__date_joined', 'profile__last_login',

        # 'Approval' Data
        'approval__approval',

        # Hacker Model
        'firstName', 'middleName', 'lastName', 'email', 'nationality',

        # 'Academic Data'
        'academic__college', 'academic__graduation', 'academic__degree',
        'academic__major', 'academic__comments'

        # 'Hackathon Application'
        'application__address_line_1', 'application__address_line_2',
        'application__city', 'application__zip', 'application__state',
        'application__country', 'application__addressVisible',


        # Skills Data
        'skills__otherDegrees', 'skills__spokenLanguages',
        'skills__programmingLanguages', 'skills__areasOfInterest',
        'skills__alumniMentor',
    )


    # Actions

    xslx_export = export_as_xslx_action("Export as XSLX",
                                        fields=full_export_fields)

    actions = [
        'xslx_export',
        'csv_export'
    ]

    def fullName(self, x):
        return x.fullName
    fullName.short_description = 'Full Name'

    def userApproval(self, x):
        return x.approval.approval
    userApproval.short_description = 'Approved'
    userApproval.boolean = 'true'
    userApproval.admin_order_field = 'approval__approval'

    def completedSetup(self, x):# TODO: Use last field
        try:
            if x.skills:
                return True
            else:
                return False
        except:
            return False
    completedSetup.short_description = 'Setup Done'
    completedSetup.boolean = True
    completedSetup.admin_order_field = 'skills__id'


admin.site.register(Hacker, HackerAdmin)

from django.contrib.auth.models import Group
admin.site.unregister(Group)