# protoc --proto_path=. --java_out=java --grpc_java_out=java vandal.proto
PROTO_COMMAND_OUTPUT=$(./manage.py garuda)
echo $PROTO_COMMAND_OUTPUT
python -m grpc_tools.protoc -I garuda_dir --python_out=garuda_dir --grpc_python_out=garuda_dir garuda_dir/garuda.proto
protoc -I garuda_dir garuda_dir/garuda.proto --go_out=plugins=grpc:garuda_dir
grpc_tools_node_protoc -I garuda_dir --js_out=import_style=commonjs,binary:garuda_dir --grpc_out=garuda_dir --plugin=protoc-gen-grpc=`which grpc_tools_node_protoc_plugin` garuda_dir/garuda.proto
# sed -i 's/import vandal_pb2 as vandal__pb2/import vandal.proto.vandal_pb2 as vandal__pb2/g' vandal/proto/vandal_pb2.py vandal/proto/vandal_pb2_grpc.py
# grep -q -F 'exports.grpc = grpc;' vandal/proto/vandal_grpc_pb.js || echo 'exports.grpc = grpc;' >> vandal/proto/vandal_grpc_pb.js
