import time
import grpc
from concurrent import futures
from importlib import import_module

from django.core.management.base import BaseCommand
from garuda.constants import GARUDA_DIR, GARUDA_PORT

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

garuda_grpc = import_module(f'{GARUDA_DIR}.garuda_pb2_grpc')


class Command(BaseCommand):
    help = 'Garuda gRPC server'

    def handle(self, *args, **options):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        servicer = garuda_grpc.GarudaServicer()
        garuda_grpc.add_GarudaServicer_to_server(servicer, server)
        server.add_insecure_port(f'[::]:{GARUDA_PORT}')
        server.start()
        print(f'server started on port {GARUDA_PORT} ...')
        try:
            while True:
                time.sleep(_ONE_DAY_IN_SECONDS)
        except KeyboardInterrupt:
            server.stop(0)
