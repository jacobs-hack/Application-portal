from django.contrib import admin

from hacker.actions import export_as_xslx_action
from .models import Hacker, HackathonApplication, \
    AcademicData, Approval, Organizational, CV, RSVP

class HackerApprovalInline(admin.StackedInline):
    model = Approval

class HackerRSVPInline(admin.StackedInline):
    model = RSVP


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

class ApprovalFilter(admin.SimpleListFilter):
    title = 'Approval'
    parameter_name = 'approval'
    
    def lookups(self, request, modeladmin):
        return [
            ('true',  'Accepted'), 
            ('false', 'Rejected'),
            ('null',  'Pending')
        ]
    
    def queryset(self, request, queryset):
        if self.value() == 'true':
            return queryset.filter(approval__approval=True)
        elif self.value() == 'false':
            return queryset.filter(approval__approval=False)
        elif self.value() == 'null':
            return queryset.filter(approval__isnull=True)
        else:
            return queryset


class HackerAdmin(admin.ModelAdmin):
    inlines = [
        HackerApprovalInline,
        HackerRSVPInline,
        HackerAcademicDataInline,
        HackerHackathonApplicationInline,
        HackerOrganizationalInline,
        HackerCVIncline
    ]

    # Fields that should be searchable
    search_fields = [
        'firstName', 'middleName', 'lastName', 'email', 'academic__school',
    ]

    # Fields that are displayed in the admin view
    list_display = (
        # basic information
        'fullName', 'email', 'userApproval', 'userRSVP', 'completedSetup',

        'school', 'degree', 'year',

        'shirtSize', 'needVisa', 'needReimbursement'
    )

    # Fields that can be dynamically filtered for
    list_filter = (
        ApprovalFilter, 'rsvp__going', SetupCompleted, 

        'academic__school', 'academic__degree', 'academic__year',

        'application__firstHackathon',

        'organizational__shirtSize', 'organizational__needVisa', 'organizational__needReimbursement',
    )

    # List of all fields, for the xslx export

    full_export_fields = (
        # Profile data
        'profile__username', 'profile__is_staff', 'profile__is_superuser',
        'profile__date_joined', 'profile__last_login',

        # Consent
        'jacobsHackTerms', 'mlhCodeOfConduct', 'mlhContestTerms',

        # 'Approval' Data
        'approval__approval',

        # 'RSVP' data
        'rsvp__going',

        # Hacker Model
        'firstName', 'middleName', 'lastName', 
        'dob', 'gender', 'race',
        'email', 'phoneNumber', 
        'nationality', 'countryOfResidence',

        # Academic Data
        'academic__school', 'academic__degree', 'academic__major', 'academic__year',

        # Hackathon Application
        'application__whyJacobsHack', 'application__firstHackathon',
        'application__whatHaveYouBuilt',


        # Organizational Data
        'organizational__shirtSize', 'organizational__needVisa', 'organizational__passportNumber', 
        'organizational__dietaryRequirements', 'organizational__comments'
    )


    # Actions
    def get_actions(self, request):
        actions = super(HackerAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


    xslx_export = export_as_xslx_action("Export as XSLX",
                                        fields=full_export_fields)
    
    # Approval and rejection options
    def approve_hacker(modeladmin, request, queryset):
        for hacker in queryset:
            (approval, created) = Approval.objects.get_or_create(hacker=hacker)
            approval.approval = True
            approval.save()
    approve_hacker.short_description = "Approve Application(s)"
    
    def reject_hacker(modeladmin, request, queryset):
        for hacker in queryset:
            (approval, created) = Approval.objects.get_or_create(hacker=hacker)
            approval.approval = False
            approval.save()
    reject_hacker.short_description = "Reject Application(s)"

    def autopend_hackers(modeladmin, request, queryset):
        for hacker in queryset:
            try:
                hacker.approval.delete()
            except Approval.DoesNotExist:
                pass
    autopend_hackers.short_description = "Pendify Applications(s)"

    actions = [
        'xslx_export',
        'csv_export',

        'approve_hacker',
        'reject_hacker',
        'autopend_hackers'
    ]

    def fullName(self, x):
        return x.fullName
    fullName.short_description = 'Full Name'

    def userApproval(self, x):
        return x.approval.approval
    userApproval.short_description = 'Approved'
    userApproval.boolean = 'true'
    userApproval.admin_order_field = 'approval__approval'

    def userRSVP(self, x):
        return x.rsvp.going
    userRSVP.short_description = 'RSVP'
    userRSVP.boolean = 'true'
    userRSVP.admin_order_field = 'rsvp__going'

    def school(self, x):
        return x.academic.school
    school.short_description = 'School'
    school.admin_order_field = 'academic__school'

    def degree(self, x):
        return x.academic.degree
    degree.short_description = 'Degree'
    degree.admin_order_field = 'academic__degree'

    def year(self, x):
        return x.academic.year
    year.short_description = 'Year'
    year.admin_order_field = 'academic__year'

    def shirtSize(self, x):
        return x.organizational.shirtSize
    shirtSize.short_description = 'Shirt Size'
    shirtSize.admin_order_field = 'organizational__shirtSize'

    def needVisa(self, x):
        return x.organizational.needVisa
    needVisa.short_description = 'Visa'
    needVisa.boolean = True
    needVisa.admin_order_field = 'organizational__needVisa'

    def needReimbursement(self, x):
        return x.organizational.needReimbursement
    needReimbursement.short_description = 'Reimbursment'
    needReimbursement.boolean = True
    needReimbursement.admin_order_field = 'organizational__needReimbursement'

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