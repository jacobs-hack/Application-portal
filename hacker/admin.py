from django.contrib import admin

from hacker.actions import export_as_csv_action, export_as_xslx_action
from .models import Alumni, Address, JobInformation, SocialMedia, \
    JacobsData, Approval, PaymentInformation, Skills


class AlumniJacobsDataInline(admin.StackedInline):
    model = JacobsData


class AlumniSocialMediaInline(admin.StackedInline):
    model = SocialMedia


class AlumniAddressInline(admin.StackedInline):
    model = Address


class AlumniJobsInline(admin.StackedInline):
    model = JobInformation


class AlumniApprovalInline(admin.StackedInline):
    model = Approval


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


class AlumniAdmin(admin.ModelAdmin):
    inlines = [AlumniApprovalInline, AlumniAddressInline,
               AlumniSocialMediaInline, AlumniJacobsDataInline,
               AlumniJobsInline, SkillsInline]

    # search through names and emails
    search_fields = ['firstName', 'middleName', 'lastName', 'email',
                     'existingEmail', 'approval__gsuite']

    list_display = (
        # basic information
        'fullName', 'email', 'userApproval', 'completedSetup', 'userGSuite', 'sex', 'birthday',
        'category',

        # Jacobs information
        'jacobs_degree', 'jacobs_graduation', 'jacobs_major', 'jacobs_college',
    )

    list_filter = (
        'approval__approval', SetupCompleted, 'category', 'jacobs__degree',
        'jacobs__graduation',
        'jacobs__major')

    legacy_export_fields = list_display + ('existingEmail',
                                           'resetExistingEmailPassword')
    csv_export = export_as_csv_action("Export as CSV (Legacy)",
                                      fields=legacy_export_fields)

    full_export_fields = (
        # Profile data
        'profile__username', 'profile__is_staff', 'profile__is_superuser',
        'profile__date_joined', 'profile__last_login',

        # Alumni Model
        'firstName', 'middleName', 'lastName', 'email', 'existingEmail',
        'resetExistingEmailPassword', 'sex', 'birthday', 'birthdayVisible',
        'nationality', 'category',

        # Address Data
        'address__address_line_1', 'address__address_line_2', 'address__city',
        'address__zip', 'address__state', 'address__country',
        'address__addressVisible',

        # 'Social' Data
        'social__facebook', 'social__linkedin', 'social__twitter',
        'social__instagram', 'social__homepage',

        # 'Jacobs Data'
        'jacobs__college', 'jacobs__graduation', 'jacobs__degree',
        'jacobs__major', 'jacobs__comments'

        # 'Approval' Data
                         'approval__approval',

        # Job Data
        'job__employer', 'job__position', 'job__industry', 'job__job',

        # Skills Data
        'skills__otherDegrees', 'skills__spokenLanguages',
        'skills__programmingLanguages', 'skills__areasOfInterest',
        'skills__alumniMentor',
    )
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

    def userGSuite(self, x):
        return x.approval.gsuite
    
    userGSuite.short_description = 'Alumni E-Mail'
    userGSuite.admin_order_field = 'approval__gsuite'

    def jacobs_degree(self, x):
        return x.jacobs.degree

    jacobs_degree.short_description = 'Degree'
    jacobs_degree.admin_order_field = 'jacobs__degree'

    def jacobs_graduation(self, x):
        return x.jacobs.graduation

    jacobs_graduation.short_description = 'Class'
    jacobs_graduation.admin_order_field = 'jacobs__graduation'

    def jacobs_major(self, x):
        return x.jacobs.major

    jacobs_major.short_description = 'Major'
    jacobs_major.admin_order_field = 'jacobs__major'

    def jacobs_college(self, x):
        return x.jacobs.college

    jacobs_college.short_description = 'College'
    jacobs_college.admin_order_field = 'jacobs__college'


admin.site.register(Alumni, AlumniAdmin)

from django.contrib.auth.models import Group
admin.site.unregister(Group)