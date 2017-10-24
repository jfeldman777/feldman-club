from django.conf.urls import url

from .views2 import pre_quiz, exam, pre_final, final, exam_next, exam_prev
from .views import QuizListView, CategoriesListView,\
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList,\
    QuizMarkingDetail, QuizDetailView, QuizTake


urlpatterns =         [url(regex=r'^$',
                           view=QuizListView.as_view(),
                           name='quiz_index'),

                       url(regex=r'^category/$',
                           view=CategoriesListView.as_view(),
                           name='quiz_category_list_all'),

                       url(regex=r'^category/(?P<category_name>[\w|\W-]+)/$',
                           view=ViewQuizListByCategory.as_view(),
                           name='quiz_category_list_matching'),

                       url(regex=r'^progress/$',
                           view=QuizUserProgressView.as_view(),
                           name='quiz_progress'),

                       url(regex=r'^marking/$',
                           view=QuizMarkingList.as_view(),
                           name='quiz_marking'),

                       url(regex=r'^marking/(?P<pk>[\d.]+)/$',
                           view=QuizMarkingDetail.as_view(),
                           name='quiz_marking_detail'),

                       url(regex=r'^final/$',
                           view=final,
                           name='final'),

                       url(regex=r'^pre_final/$',
                           view=pre_final,
                           name='pre_final'),


                       url(regex=r'^exam/next/$',
                           view=exam_next,
                           name='exam_next'),

                      url(regex=r'^exam/prev/$',
                          view=exam_prev,
                          name='exam_prev'),


                       url(regex=r'^exam/$',
                           view=exam,
                           name='exam'),

                       url(regex=r'^(?P<slug>[\w-]+)/$',
                           view=pre_quiz,
                           name='pre_quiz'),


                           ]
