import django_filters
from afritechjobsapi.models import Category, JobLevel, JobLocations, JobSkills, JobType, PostAJob

class CategoryFilter(django_filters.FilterSet):
    # http://127.0.0.1:8000/jobs/category/?name=admin
    name = django_filters.CharFilter(field_name='name', lookup_expr='iexact')

    class Meta:
        model = Category
        fields = ['name']

class JobLevelFilter(django_filters.FilterSet):
    # http://127.0.0.1:8000/jobs/level?job_level=midlevel
    job_level = django_filters.CharFilter(field_name='job_level_choices', lookup_expr='iexact')

    class Meta:
        model = JobLevel
        fields = ['job_level_choices']

class JobLocationsFilter(django_filters.FilterSet):
    # http://127.0.0.1:8000/jobs/locations/?name=abUja
    name = django_filters.CharFilter(field_name='name', lookup_expr='iexact')

    class Meta:
        model = JobLocations
        fields = ['name']

class JobTypeFilter(django_filters.FilterSet):
    # http://127.0.0.1:8000/jobs/type/?job_type=FULLTIME
    job_type = django_filters.CharFilter(field_name='job_type_choices', lookup_expr='iexact')

    class Meta:
        model = JobType
        fields = ['job_type_choices']

class JobSkillsFilter(django_filters.FilterSet):
    # http://127.0.0.1:8000/jobs/type/?title=remote
    title = django_filters.CharFilter(field_name='title', lookup_expr='iexact')

    class Meta:
        model = JobSkills
        fields = ['title']

class PostAJobFilter(django_filters.FilterSet):
    job_category = django_filters.CharFilter(field_name="job_category__name", lookup_expr="iexact")
    job_type = django_filters.CharFilter(field_name="job_type__job_type_choices", lookup_expr="iexact")
    job_level = django_filters.CharFilter(field_name="job_level__job_level_choices", lookup_expr="iexact")
    job_location = django_filters.CharFilter(field_name="job_location__name", lookup_expr="iexact")
    job_skills = django_filters.CharFilter(field_name="job_skills__title", lookup_expr="iexact")
    class Meta:
        model = PostAJob
        fields = ['job_category', 'job_type', 'job_level', 'job_location', 'job_skills']
