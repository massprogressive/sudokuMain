#!/usr/bin/env python3
import click
import sys
import os
from sudoku.functions import *
from sudoku.Solver import *

@click.command()
@click.option('--path', default='sudoku/boards/easy_01.txt',
            help='''Path to text file with board inside.
            Board in the file should looks like default
            example in board_easy.txt
            '''
)

def cli(path):
    """
    This programs allows you to solve any sudoku puzzle, if it's possible to
    solve.
    """
    if os.path.isfile(path):
        solution = run(Solver, path)
        click.echo(solution)
    else:
        click.echo('Nothing to solve')

if __name__ == '__main__':
    path = input('Path to file: ')
    if os.path.isfile(path):
        run(Solver, path)
    else:
        run(Solver, os.path.abspath('/sudoku/boards/easy_01.txt'))
