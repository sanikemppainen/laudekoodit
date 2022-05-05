from invoke import task


@task
def start(ctx):
    ctx.run("flask run")


@task
def format(ctx):
    ctx.run("black .")
