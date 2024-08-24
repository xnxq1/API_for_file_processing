from datetime import date

from pydantic import BaseModel, EmailStr, field_validator


class SchemasUser(BaseModel):

    email: EmailStr
    username: str
    date_of_birth: date
    phone_number: str


    @field_validator('phone_number')
    @classmethod
    def validate_phone_number(cls, phone_number: str):
        if phone_number[0] != '+':
            raise ValueError('Номер телефона должен начинаться с +')
        if len(phone_number) > 15 or len(phone_number) < 7:
            raise ValueError('Длина номера должна быть от 7 до 15 символов.')
        for el in phone_number[1:]:
            if not el.isdigit():
                raise ValueError('Номер телефона должен содержать только цифры')
        return phone_number

class SchemasUserForRegister(SchemasUser):
    password: str


class SchemasUserForAuth(BaseModel):
    email: EmailStr
    password: str
