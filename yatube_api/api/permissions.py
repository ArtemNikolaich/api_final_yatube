from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorOrReadOnly(BasePermission):
    """
    Пермишен, позволяющий только автору объекта выполнять изменения,
    в то время как остальным пользователям доступно только чтение (GET).
    """
    def has_permission(self, request, view):
        """
        Проверяет, имеет ли пользователь разрешение на доступ к представлению.
        """
        return request.method in SAFE_METHODS or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Проверяет, имеет ли пользователь разрешение на доступ к объекту.
        """
        return request.method in SAFE_METHODS or obj.author == request.user
