from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import Payment
from .serializers import PaymentSerializer

from profiles.models import Profile
from profiles.serializers import PeriodEmployeeStatisticsSerializer


class GetPaymentsView(ListAPIView):
    """
    Вывод списка выплат пользователя. Доступно всем кроме админа.
    """
    serializer_class = PaymentSerializer
    permission_classes = [~IsAdminUser]

    def get_queryset(self):
        try:
            user = self.request.user
            user_profile = Profile.objects.get(user=user)
            return Payment.objects.filter(employee=user_profile)
        except Exception as e:
            return Response({"message": f"Пользователь не найден.\n {e}"}, status=404)


class GetEmployeeStatisticsView(ListAPIView):
    """
    Вывод статистики по сотрудникам и их итоговым выплатам. Доступно админу.
    """
    serializer_class = PeriodEmployeeStatisticsSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        try:
            if department := self.request.GET.get('department'):
                return Profile.objects.filter(department=department)
            return Profile.objects.all()
        except Exception as e:
            return Response({"message": f"Ошибка. \n {e}"})


class MakePaymentsView(GenericAPIView):
    """
    Зафиксировать выплаты сотрудникам в зависимости от их наработанных часов.
    Доступно админу.
    """
    permission_classes = [IsAdminUser]

    def post(self, request):
        try:
            for employee in Profile.objects.all():
                Payment.objects.create(
                    employee=employee, amount=(employee.hourly_rate * employee.hours)
                )
            return Response({"message": "Выплаты созданы успешно."}, status=200)
        except Exception as e:
            return Response({"message": f"Произошла ошибка.\n {e}"})
