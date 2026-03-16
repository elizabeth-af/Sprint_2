class EmployeeSalary:

   hourly_payment = 400
   def __init__(self, name, hours, rest_days, email):
       self.name = name
       self.hours = hours
       self.rest_days = rest_days
       self.email = email

   @classmethod
   def get_hours(cls, name, hours, rest_days, email):
       if hours == None:
            hours = (7 - rest_days) * 8
       return cls(name, hours, rest_days, email)

   @classmethod
   def get_email(cls, name, hours, rest_days, email):
       if email == None:
           email = name + '@email.com'
       return cls(name, hours, rest_days, email)

   @classmethod
   def set_hourly_payment(cls, hourly_payment):
       cls.hourly_payment = hourly_payment
       return cls.hourly_payment

   @staticmethod
   def salary(hours, hourly_payment):
       return hours * hourly_payment

new = EmployeeSalary.get_email('имя', 6, 2, None)
print(new.name, new.hours, new.rest_days, new.email)
print(EmployeeSalary.set_hourly_payment(89))
print(new.salary(new.hours, new.hourly_payment))