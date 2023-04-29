from random import randint

from django.core.management.base import BaseCommand

from web.models import Project, Skill


class Command(BaseCommand):
    def handle(self, *args, **options):
        skills = Skill.objects.all()
        projects = []
        for i in range(30):
            for j in range(randint(5, 10)):
                projects.append(Project(name=f'generated project {i}-{j} NAME',
                                        description=f'generated project {i}-{j} DESCRIPTION',
                                        rate=randint(0, 10)), )

        saved_projects = Project.objects.bulk_create(projects)

        project_skills = []

        for project in saved_projects:
            count_of_skills = randint(0, len(skills))
            for skill_index in range(count_of_skills):
                project_skills.append(Project.skills.through(project_id=project.id, skill_id=skills[skill_index].id))

        Project.skills.through.objects.bulk_create(project_skills)
