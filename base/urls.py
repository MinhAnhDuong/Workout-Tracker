from django.urls import path
from .views import ExerciseList, ExerciseDetail, ExerciseCreate, ExerciseUpdate, ExerciseDelete, TrainingRecordCreate, TrainingRecordDelete, TrainingRecordDetail, TrainingRecordDeleteSuccess, TrainingRecordUpdate

urlpatterns = [
    #exercise
    path('exercises/', ExerciseList.as_view(), name='exercises'),
    path('exercises/exercise/<int:pk>/', ExerciseDetail.as_view(), name='exercise'),
    path('exercises/exercise-create/', ExerciseCreate.as_view(), name= 'exercise-create'),
    path('exercises/exercise-update/<int:pk>/', ExerciseUpdate.as_view(), name='exercise-update'),
    path('exercises/exercise-delete/<int:pk>/', ExerciseDelete.as_view(), name='exercise-delete'),

    #training record
    path('exercises/record/<int:pk>/', TrainingRecordDetail.as_view(), name='record'),
    path('exercises/exercise/<int:pk>/record-create/', TrainingRecordCreate.as_view(), name='record-create'),
    path('exercises/record-delete/<int:pk>/', TrainingRecordDelete.as_view(), name='record-delete'),
    path('exercises/record-update/<int:pk>/', TrainingRecordUpdate.as_view(), name='record-update'),
    path('exercises/record-delete-success/', TrainingRecordDeleteSuccess.as_view(), name='record-delete-success'),
]
