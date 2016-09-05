#!/usr/bin/env python3
import click

from .Solver import Solver
from .functions import run


@click.command()
@click.argument(
    'input_file',
    type=click.File('r'),
)
def cli(path):
    """
    This programs allows you to solve any sudoku puzzle,
    if it's possible to solve.
    """
    solution = run(Solver, path)
    click.echo(solution)
