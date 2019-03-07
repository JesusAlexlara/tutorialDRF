from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import GenericPollList, GenericPollDetail, GenericChoiceList, GenericCreateVote
from .views import GenericChoiceList, CreateVote, PollViewSet

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [

    path('polls/<int:pk>/choices', GenericChoiceList.as_view(), name='choice_list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote', CreateVote.as_view(), name='create_vote'),

    # path('polls/', GenericPollList.as_view(), name="polls_list"),
    # path('polls/<int:pk>', GenericPollDetail.as_view(), name="polls_detail"),
    # path('choice/', GenericChoiceList.as_view(), name="choice_list"),
    # path('vote/', GenericCreateVote.as_view(), name="create_vote")
]

urlpatterns += router.urls
