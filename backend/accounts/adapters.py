from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        # 기본 저장 필드: first_name, last_name, username, email
        user = super().save_user(request, user, form, False)
        # 추가 저장 필드: nickname, gender, age, phone
            
        nickname=data.get("nickname")
        if nickname:
            user.nickname=nickname
            
        gender=data.get("gender")
        if gender:
            user.gender=gender
            
        age=data.get("age")
        if age:
            user.age=age
            
        phone=data.get("phone")
        if phone:
            user.phone=phone
            
        

        user.save()
        return user