from datetime import timedelta

from django.contrib.contenttypes.models import ContentType
from django.utils.timezone import now

import factory
import factory.fuzzy

from bluebottle.bb_tasks import get_task_model
from bluebottle.bb_tasks.models import TaskMember, Skill
from .accounts import BlueBottleUserFactory
from .projects import ProjectFactory

TASK_MODEL = get_task_model()


class SkillFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Skill

    name = factory.Sequence(lambda n: 'Skill_{0}'.format(n))
    name_nl = factory.LazyAttribute(lambda o: o.name)


class TaskFactory(factory.DjangoModelFactory):
    FACTORY_FOR = TASK_MODEL

    author = factory.SubFactory(BlueBottleUserFactory)
    project = factory.SubFactory(ProjectFactory)
    skill = factory.SubFactory(SkillFactory)
    title = factory.Sequence(lambda n: 'Task_{0}'.format(n))
    deadline = factory.fuzzy.FuzzyDateTime(now(), now() + timedelta(weeks=4))


class ContentTypeFactory(factory.DjangoModelFactory):
    FACTORY_FOR = ContentType

    name = TASK_MODEL._meta.verbose_name.title()
    app_label = 'bb_tasks'
    model = TASK_MODEL.__class__.__name__


class TaskMemberFactory(factory.DjangoModelFactory):
    FACTORY_FOR = TaskMember

    member = factory.SubFactory(BlueBottleUserFactory)
    status = 'accepted'
    content_type = factory.SubFactory(ContentTypeFactory)
    task_id = 1
    task = factory.SubFactory(TaskFactory)
