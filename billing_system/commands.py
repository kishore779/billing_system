import click

@click.command()
def welcome():
    print("This is a custom cammand")

commands = [welcome]