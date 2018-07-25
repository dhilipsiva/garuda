import time
import grpc
from concurrent import futures
from importlib import import_module

from django.core.management.base import BaseCommand
from garuda.constants import GARUDA_DIR, GARUDA_PORT, GARUDA_AUTO_MODULE

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

auto_garuda = import_module(GARUDA_AUTO_MODULE)
garuda_grpc = import_module(f'{GARUDA_DIR}.garuda_pb2_grpc')


class Servicer(auto_garuda.AutoGaruda, garuda_grpc.GarudaServicer):
    pass


class Command(BaseCommand):
    help = 'Garuda gRPC server'

    def handle(self, *args, **options):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        garuda_grpc.add_GarudaServicer_to_server(Servicer(), server)
        server.add_insecure_port(f'[::]:{GARUDA_PORT}')
        server.start()
        print(f'server started on port {GARUDA_PORT} ...')
        try:
            while True:
                time.sleep(_ONE_DAY_IN_SECONDS)
        except KeyboardInterrupt:
            server.stop(0)
