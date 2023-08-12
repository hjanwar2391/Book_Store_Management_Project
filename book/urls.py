from django.urls import path
from book.views import home, storebook, showbook, editbook,deleteBook

urlpatterns = [
    path('', home, name='homes'),
    path("storebook/", storebook, name="storebook"),
    path("showbook/", showbook, name="showbook" ),
    path("editbook/<int:id>", editbook, name="editbook" ),
    path('deleteBook/<int:id>', deleteBook, name='deleteBook'),
]
