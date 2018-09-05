#!/usr/bin/env python
from socialpy import SOCIALPY_KEY_FILE, API_NAMES, POST_STATUS
from socialpy.data import Post, Category
from socialpy.client import Gateway

import argparse
from tabulate import tabulate
from django.db.models import Sum
from django.db.models import Count

def print_post(args):
    post = Post.objects.filter(id=args.id).first()

    if post:
        print('\nid: {}   status: {}    [{}]\ncategorys: {}\ntext: {}\nimage: {}'.format(
            post.id,
            post.status,
            post.created.strftime('%Y-%m-%d %H:%M'),
            ", ".join([item.name for item in post.categorys.all()]),
            post.text,
            post.image.name,
        ))
    else:
        print('\nNo post with id {}!'.format(args.id))

def main():
    parser = argparse.ArgumentParser(description='SocialPy | DATA')

    parser.add_argument('action', nargs='?', type=str, choices=['show', 'stat', 'post'])
    parser.add_argument('--id', type=int, help='The ID of the post')

    parser.add_argument(
        '--order', type=str, default='?',
        help='Filter with status.To change diraction uses +, becose argparse didnt like -')

    parser.add_argument(
        '--limit', type=int,
        help='Limit the post list')

    parser.add_argument(
        '--status', type=str, default='new',
        choices=POST_STATUS,
        help='Filter with status')

    parser.add_argument(
        '--networks', type=str, nargs='+',
        choices=API_NAMES,
        help='...')

    parser.add_argument(
        '--format', type=str, default='orgtbl',
        choices=[
            'plain', 'simple', 'grid', 'pipe', 'orgtbl', 'rst',
            'mediawiki', 'latex'
        ],
        help='Set the format of the table.')

    args = parser.parse_args()

    if args.id:
        print_post(args)
        exit()

    q = Post.objects.filter(status=args.status).order_by(args.order.replace('+', '-')).all()

    if args.limit:
        q = q[:args.limit]#.limit(args.limit)

    if args.action == 'show':
        table = []
        for post in q:
            table.append([
                post.id,
                post.status,
                post.created.strftime('%Y-%m-%d %H:%M'),
                'yes' if post.text else 'no',
                'yes' if post.image.name else 'no',
                ", ".join([item.name for item in post.categorys.all()]),
            ])

        headers = ['id', 'status', 'created', 'text', 'image', 'categorys']

        print('')
        print(tabulate(table, headers, tablefmt=args.format))
        exit()

    if args.action == 'post':
        gateway = Gateway()
        gateway.load_from_file(SOCIALPY_KEY_FILE)

        # delete apis from gatway if not in networks
        if args.networks:
            gateway.clear(args.networks)

        # post it on every api in the gateway
        for post in q:
            gateway.post(**post.kwargs())
            for n in gateway.apis:
                post.poston.create(network=n)

        exit()

    if args.action == 'stat':
        headers = ['post', 'count']
        table = []
        table.append(['total', Post.objects.filter(status='new').count()])
        for data in Category.objects.filter(posts__status='new').annotate(count=Count('posts')):
            table.append([data, data.count])

        table.append(['text', Post.objects.filter(status='new').exclude(text='').count()])
        table.append(['image', Post.objects.filter(status='new').exclude(image='').count()])

        print('')
        print(tabulate(table, headers, tablefmt=args.format))
        exit()

    parser.print_help()



if __name__ == "__main__":
    main()
