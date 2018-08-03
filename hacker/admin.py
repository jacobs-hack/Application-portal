from django.contrib import admin

from hacker.actions import export_as_xslx_action
from .models import Hacker, HackathonApplication, \
    AcademicData, Approval, Organizational, CV

class HackerApprovalInline(admin.StackedInline):
    model = Approval


class HackerAcademicDataInline(admin.StackedInline):
    model = AcademicData


class HackerHackathonApplicationInline(admin.StackedInline):
    model = HackathonApplication


class HackerOrganizationalInline(admin.StackedInline):
    model = Organizational

class HackerCVIncline(admin.StackedInline):
    model = CV

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
            return queryset.filter(organizational__isnull=False)
        elif self.value() == '0':
            return queryset.filter(organizational__isnull=True)
        else:
            return queryset


class HackerAdmin(admin.ModelAdmin):
    inlines = [
        HackerApprovalInline,
        HackerAcademicDataInline,
        HackerHackathonApplicationInline,
        HackerOrganizationalInline,
        HackerCVIncline
    ]

    # Fields that should be searchable
    search_fields = [
        'firstName', 'middleName', 'lastName', 'email', 'academic__university',
    ]

    # Fields that are displayed in the admin view
    list_display = (
        # basic information
        'fullName', 'email', 'userApproval', 'completedSetup',

        'university', 'degree', 'year',

        'shirtSize',
    )

    # Fields that can be dynamically filtered for
    list_filter = (
        'approval__approval', SetupCompleted,

        'academic__university', 'academic__degree', 'academic__year',

        'application__firstHackathon',

        'organizational__shirtSize',
    )

    # List of all fields, for the xslx export

    full_export_fields = (
        # Profile data
        'profile__username', 'profile__is_staff', 'profile__is_superuser',
        'profile__date_joined', 'profile__last_login',

        # Consent
        'jacobsHackTerms', 'mlhCodeOfConduct', 'mlhContestTerms', 'mlhSharingConsent',

        # 'Approval' Data
        'approval__approval',

        # Hacker Model
        'firstName', 'middleName', 'lastName', 'email', 'phoneNumber', 'nationality', 'countryOfResidence',

        # Academic Data
        'academic__university', 'academic__degree', 'academic__year',

        # Hackathon Application
        'application__whyJacobsHack', 'application__firstHackathon',
        'application__whatHaveYouBuilt',


        # Organizational Data
        'organizational__shirtSize', 'organizational__needVisa',
        'organizational__dietaryRequirements', 'organizational__comments'
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

    def university(self, x):
        return x.academic.university
    university.short_description = 'University'
    university.admin_order_field = 'academic__university'

    def degree(self, x):
        return x.academic.degree
    university.short_description = 'Degree'
    university.admin_order_field = 'academic__degree'

    def year(self, x):
        return x.academic.year
    university.short_description = 'Year'
    university.admin_order_field = 'academic__year'

    def shirtSize(self, x):
        return x.organizational.shirtSize
    shirtSize.short_description = 'Shirt Size'
    shirtSize.admin_order_field = 'organizational__shirtSize'

    def completedSetup(self, x):
        try:
            if x.organizational:
                return True
            else:
                return False
        except:
            return False
    completedSetup.short_description = 'Setup Done'
    completedSetup.boolean = True
    completedSetup.admin_order_field = 'organizational__id'


admin.site.register(Hacker, HackerAdmin)

from django.contrib.auth.models import Group
admin.site.unregister(Group)