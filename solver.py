#!/usr/bin/env python3
import click
import sys
import os
from sudoku.functions import *
from sudoku.Solver import *

@click.command()
@click.option('--path', default='',
            help='Path to file'
)

def cli(path):
    if os.path.isfile(path):
        solution = run(Solver, path)
        click.echo(solution)
    else:
        click.echo('Nothing to solve')
