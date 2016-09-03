#!/usr/bin/env python3
import click
import sys
import os
from sudoku.functions import *
from sudoku.Solver import *

@click.command()
@click.option('--path', default='board_easy.txt',
            help='Path to text file with board inside'
)

def cli(path):
    if os.path.isfile(path):
        solution = run(Solver, path)
        # click.echo('Initial board')
        # click.echo(solution[0])
        click.echo(solution[1])
    else:
        click.echo('Nothing to solve')

if __name__ == '__main__':
    run(Solver, 'board_easy.txt')
