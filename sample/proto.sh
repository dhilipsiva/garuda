# protoc -I garuda_dir garuda_dir/garuda.proto --csharp_out=GarudaCSharp
# protoc -I garuda_dir garuda_dir/garuda.proto --js_out=import_style=commonjs,binary:node_client
grpc_tools_node_protoc -I garuda_dir --js_out=import_style=commonjs,binary:node_client --grpc_out=node_client --plugin=protoc-gen-grpc=/home/linuxbrew/.linuxbrew/bin/grpc_tools_node_protoc_plugin garuda_dir/garuda.proto

