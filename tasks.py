from invoke import task


@task
def run(ctx):
    ctx.run('python manage.py runserver')


@task
def prod(ctx):
    ctx.run('exec gunicorn -c gunicorn.conf.py --preload todo.wsgi')


@task
def migrate(ctx):
    ctx.run('python manage.py makemigrations')


@task
def upgrade(ctx):
    ctx.run('python manage.py migrate')


@task
def upstatic(ctx):
    ctx.run('python manage.py collectstatic --no-input --clear')
