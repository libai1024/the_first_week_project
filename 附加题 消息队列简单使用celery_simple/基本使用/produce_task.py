from celery_task import send_email
result = send_email.delay("yuan")
print(result.id)
result2 = send_email.delay("alex")
print(result2.id)