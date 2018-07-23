# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import garuda_pb2 as garuda__pb2


class GarudaStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.DeleteLogEntry = channel.unary_unary(
        '/garuda.Garuda/DeleteLogEntry',
        request_serializer=garuda__pb2.ID.SerializeToString,
        response_deserializer=garuda__pb2.Void.FromString,
        )
    self.UpdateLogEntry = channel.unary_unary(
        '/garuda.Garuda/UpdateLogEntry',
        request_serializer=garuda__pb2.LogEntry.SerializeToString,
        response_deserializer=garuda__pb2.Void.FromString,
        )
    self.ReadLogEntry = channel.unary_unary(
        '/garuda.Garuda/ReadLogEntry',
        request_serializer=garuda__pb2.ID.SerializeToString,
        response_deserializer=garuda__pb2.LogEntry.FromString,
        )
    self.CreateLogEntry = channel.unary_unary(
        '/garuda.Garuda/CreateLogEntry',
        request_serializer=garuda__pb2.LogEntry.SerializeToString,
        response_deserializer=garuda__pb2.LogEntry.FromString,
        )
    self.ReadLogEntrysFilter = channel.unary_stream(
        '/garuda.Garuda/ReadLogEntrysFilter',
        request_serializer=garuda__pb2.Void.SerializeToString,
        response_deserializer=garuda__pb2.LogEntry.FromString,
        )
    self.DeletePermission = channel.unary_unary(
        '/garuda.Garuda/DeletePermission',
        request_serializer=garuda__pb2.ID.SerializeToString,
        response_deserializer=garuda__pb2.Void.FromString,
        )
    self.UpdatePermission = channel.unary_unary(
        '/garuda.Garuda/UpdatePermission',
        request_serializer=garuda__pb2.Permission.SerializeToString,
        response_deserializer=garuda__pb2.Void.FromString,
        )
    self.ReadPermission = channel.unary_unary(
        '/garuda.Garuda/ReadPermission',
        request_serializer=garuda__pb2.ID.SerializeToString,
        response_deserializer=garuda__pb2.Permission.FromString,
        )
    self.CreatePermission = channel.unary_unary(
        '/garuda.Garuda/CreatePermission',
        request_serializer=garuda__pb2.Permission.SerializeToString,
        response_deserializer=garuda__pb2.Permission.FromString,
        )
    self.ReadPermissionsFilter = channel.unary_stream(
        '/garuda.Garuda/ReadPermissionsFilter',
        request_serializer=garuda__pb2.Void.SerializeToString,
        response_deserializer=garuda__pb2.Permission.FromString,
        )
    self.DeleteGroup = channel.unary_unary(
        '/garuda.Garuda/DeleteGroup',
        request_serializer=garuda__pb2.ID.SerializeToString,
        response_deserializer=garuda__pb2.Void.FromString,
        )
    self.UpdateGroup = channel.unary_unary(
        '/garuda.Garuda/UpdateGroup',
        request_serializer=garuda__pb2.Group.SerializeToString,
        response_deserializer=garuda__pb2.Void.FromString,
        )
    self.ReadGroup = channel.unary_unary(
        '/garuda.Garuda/ReadGroup',
        request_serializer=garuda__pb2.ID.SerializeToString,
        response_deserializer=garuda__pb2.Group.FromString,
        )
    self.CreateGroup = channel.unary_unary(
        '/garuda.Garuda/CreateGroup',
        request_serializer=garuda__pb2.Group.SerializeToString,
        response_deserializer=garuda__pb2.Group.FromString,
        )
    self.ReadGroupsFilter = channel.unary_stream(
        '/garuda.Garuda/ReadGroupsFilter',
        request_serializer=garuda__pb2.Void.SerializeToString,
        response_deserializer=garuda__pb2.Group.FromString,
        )
    self.DeleteUser = channel.unary_unary(
        '/garuda.Garuda/DeleteUser',
        request_serializer=garuda__pb2.ID.SerializeToString,
        response_deserializer=garuda__pb2.Void.FromString,
        )
    self.UpdateUser = channel.unary_unary(
        '/garuda.Garuda/UpdateUser',
        request_serializer=garuda__pb2.User.SerializeToString,
        response_deserializer=garuda__pb2.Void.FromString,
        )
    self.ReadUser = channel.unary_unary(
        '/garuda.Garuda/ReadUser',
        request_serializer=garuda__pb2.ID.SerializeToString,
        response_deserializer=garuda__pb2.User.FromString,
        )
    self.CreateUser = channel.unary_unary(
        '/garuda.Garuda/CreateUser',
        request_serializer=garuda__pb2.User.SerializeToString,
        response_deserializer=garuda__pb2.User.FromString,
        )
    self.ReadUsersFilter = channel.unary_stream(
        '/garuda.Garuda/ReadUsersFilter',
        request_serializer=garuda__pb2.Void.SerializeToString,
        response_deserializer=garuda__pb2.User.FromString,
        )
    self.DeleteContentType = channel.unary_unary(
        '/garuda.Garuda/DeleteContentType',
        request_serializer=garuda__pb2.ID.SerializeToString,
        response_deserializer=garuda__pb2.Void.FromString,
        )
    self.UpdateContentType = channel.unary_unary(
        '/garuda.Garuda/UpdateContentType',
        request_serializer=garuda__pb2.ContentType.SerializeToString,
        response_deserializer=garuda__pb2.Void.FromString,
        )
    self.ReadContentType = channel.unary_unary(
        '/garuda.Garuda/ReadContentType',
        request_serializer=garuda__pb2.ID.SerializeToString,
        response_deserializer=garuda__pb2.ContentType.FromString,
        )
    self.CreateContentType = channel.unary_unary(
        '/garuda.Garuda/CreateContentType',
        request_serializer=garuda__pb2.ContentType.SerializeToString,
        response_deserializer=garuda__pb2.ContentType.FromString,
        )
    self.ReadContentTypesFilter = channel.unary_stream(
        '/garuda.Garuda/ReadContentTypesFilter',
        request_serializer=garuda__pb2.Void.SerializeToString,
        response_deserializer=garuda__pb2.ContentType.FromString,
        )
    self.DeleteSession = channel.unary_unary(
        '/garuda.Garuda/DeleteSession',
        request_serializer=garuda__pb2.ID.SerializeToString,
        response_deserializer=garuda__pb2.Void.FromString,
        )
    self.UpdateSession = channel.unary_unary(
        '/garuda.Garuda/UpdateSession',
        request_serializer=garuda__pb2.Session.SerializeToString,
        response_deserializer=garuda__pb2.Void.FromString,
        )
    self.ReadSession = channel.unary_unary(
        '/garuda.Garuda/ReadSession',
        request_serializer=garuda__pb2.ID.SerializeToString,
        response_deserializer=garuda__pb2.Session.FromString,
        )
    self.CreateSession = channel.unary_unary(
        '/garuda.Garuda/CreateSession',
        request_serializer=garuda__pb2.Session.SerializeToString,
        response_deserializer=garuda__pb2.Session.FromString,
        )
    self.ReadSessionsFilter = channel.unary_stream(
        '/garuda.Garuda/ReadSessionsFilter',
        request_serializer=garuda__pb2.Void.SerializeToString,
        response_deserializer=garuda__pb2.Session.FromString,
        )
    self.DeleteArticle = channel.unary_unary(
        '/garuda.Garuda/DeleteArticle',
        request_serializer=garuda__pb2.ID.SerializeToString,
        response_deserializer=garuda__pb2.Void.FromString,
        )
    self.UpdateArticle = channel.unary_unary(
        '/garuda.Garuda/UpdateArticle',
        request_serializer=garuda__pb2.Article.SerializeToString,
        response_deserializer=garuda__pb2.Void.FromString,
        )
    self.ReadArticle = channel.unary_unary(
        '/garuda.Garuda/ReadArticle',
        request_serializer=garuda__pb2.ID.SerializeToString,
        response_deserializer=garuda__pb2.Article.FromString,
        )
    self.CreateArticle = channel.unary_unary(
        '/garuda.Garuda/CreateArticle',
        request_serializer=garuda__pb2.Article.SerializeToString,
        response_deserializer=garuda__pb2.Article.FromString,
        )
    self.ReadArticlesFilter = channel.unary_stream(
        '/garuda.Garuda/ReadArticlesFilter',
        request_serializer=garuda__pb2.Void.SerializeToString,
        response_deserializer=garuda__pb2.Article.FromString,
        )


class GarudaServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def DeleteLogEntry(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateLogEntry(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadLogEntry(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateLogEntry(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadLogEntrysFilter(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeletePermission(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdatePermission(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadPermission(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreatePermission(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadPermissionsFilter(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteGroup(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateGroup(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadGroup(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateGroup(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadGroupsFilter(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadUsersFilter(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteContentType(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateContentType(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadContentType(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateContentType(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadContentTypesFilter(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteSession(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateSession(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadSession(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateSession(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadSessionsFilter(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteArticle(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateArticle(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadArticle(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateArticle(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadArticlesFilter(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GarudaServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'DeleteLogEntry': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteLogEntry,
          request_deserializer=garuda__pb2.ID.FromString,
          response_serializer=garuda__pb2.Void.SerializeToString,
      ),
      'UpdateLogEntry': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateLogEntry,
          request_deserializer=garuda__pb2.LogEntry.FromString,
          response_serializer=garuda__pb2.Void.SerializeToString,
      ),
      'ReadLogEntry': grpc.unary_unary_rpc_method_handler(
          servicer.ReadLogEntry,
          request_deserializer=garuda__pb2.ID.FromString,
          response_serializer=garuda__pb2.LogEntry.SerializeToString,
      ),
      'CreateLogEntry': grpc.unary_unary_rpc_method_handler(
          servicer.CreateLogEntry,
          request_deserializer=garuda__pb2.LogEntry.FromString,
          response_serializer=garuda__pb2.LogEntry.SerializeToString,
      ),
      'ReadLogEntrysFilter': grpc.unary_stream_rpc_method_handler(
          servicer.ReadLogEntrysFilter,
          request_deserializer=garuda__pb2.Void.FromString,
          response_serializer=garuda__pb2.LogEntry.SerializeToString,
      ),
      'DeletePermission': grpc.unary_unary_rpc_method_handler(
          servicer.DeletePermission,
          request_deserializer=garuda__pb2.ID.FromString,
          response_serializer=garuda__pb2.Void.SerializeToString,
      ),
      'UpdatePermission': grpc.unary_unary_rpc_method_handler(
          servicer.UpdatePermission,
          request_deserializer=garuda__pb2.Permission.FromString,
          response_serializer=garuda__pb2.Void.SerializeToString,
      ),
      'ReadPermission': grpc.unary_unary_rpc_method_handler(
          servicer.ReadPermission,
          request_deserializer=garuda__pb2.ID.FromString,
          response_serializer=garuda__pb2.Permission.SerializeToString,
      ),
      'CreatePermission': grpc.unary_unary_rpc_method_handler(
          servicer.CreatePermission,
          request_deserializer=garuda__pb2.Permission.FromString,
          response_serializer=garuda__pb2.Permission.SerializeToString,
      ),
      'ReadPermissionsFilter': grpc.unary_stream_rpc_method_handler(
          servicer.ReadPermissionsFilter,
          request_deserializer=garuda__pb2.Void.FromString,
          response_serializer=garuda__pb2.Permission.SerializeToString,
      ),
      'DeleteGroup': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteGroup,
          request_deserializer=garuda__pb2.ID.FromString,
          response_serializer=garuda__pb2.Void.SerializeToString,
      ),
      'UpdateGroup': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateGroup,
          request_deserializer=garuda__pb2.Group.FromString,
          response_serializer=garuda__pb2.Void.SerializeToString,
      ),
      'ReadGroup': grpc.unary_unary_rpc_method_handler(
          servicer.ReadGroup,
          request_deserializer=garuda__pb2.ID.FromString,
          response_serializer=garuda__pb2.Group.SerializeToString,
      ),
      'CreateGroup': grpc.unary_unary_rpc_method_handler(
          servicer.CreateGroup,
          request_deserializer=garuda__pb2.Group.FromString,
          response_serializer=garuda__pb2.Group.SerializeToString,
      ),
      'ReadGroupsFilter': grpc.unary_stream_rpc_method_handler(
          servicer.ReadGroupsFilter,
          request_deserializer=garuda__pb2.Void.FromString,
          response_serializer=garuda__pb2.Group.SerializeToString,
      ),
      'DeleteUser': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteUser,
          request_deserializer=garuda__pb2.ID.FromString,
          response_serializer=garuda__pb2.Void.SerializeToString,
      ),
      'UpdateUser': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateUser,
          request_deserializer=garuda__pb2.User.FromString,
          response_serializer=garuda__pb2.Void.SerializeToString,
      ),
      'ReadUser': grpc.unary_unary_rpc_method_handler(
          servicer.ReadUser,
          request_deserializer=garuda__pb2.ID.FromString,
          response_serializer=garuda__pb2.User.SerializeToString,
      ),
      'CreateUser': grpc.unary_unary_rpc_method_handler(
          servicer.CreateUser,
          request_deserializer=garuda__pb2.User.FromString,
          response_serializer=garuda__pb2.User.SerializeToString,
      ),
      'ReadUsersFilter': grpc.unary_stream_rpc_method_handler(
          servicer.ReadUsersFilter,
          request_deserializer=garuda__pb2.Void.FromString,
          response_serializer=garuda__pb2.User.SerializeToString,
      ),
      'DeleteContentType': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteContentType,
          request_deserializer=garuda__pb2.ID.FromString,
          response_serializer=garuda__pb2.Void.SerializeToString,
      ),
      'UpdateContentType': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateContentType,
          request_deserializer=garuda__pb2.ContentType.FromString,
          response_serializer=garuda__pb2.Void.SerializeToString,
      ),
      'ReadContentType': grpc.unary_unary_rpc_method_handler(
          servicer.ReadContentType,
          request_deserializer=garuda__pb2.ID.FromString,
          response_serializer=garuda__pb2.ContentType.SerializeToString,
      ),
      'CreateContentType': grpc.unary_unary_rpc_method_handler(
          servicer.CreateContentType,
          request_deserializer=garuda__pb2.ContentType.FromString,
          response_serializer=garuda__pb2.ContentType.SerializeToString,
      ),
      'ReadContentTypesFilter': grpc.unary_stream_rpc_method_handler(
          servicer.ReadContentTypesFilter,
          request_deserializer=garuda__pb2.Void.FromString,
          response_serializer=garuda__pb2.ContentType.SerializeToString,
      ),
      'DeleteSession': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteSession,
          request_deserializer=garuda__pb2.ID.FromString,
          response_serializer=garuda__pb2.Void.SerializeToString,
      ),
      'UpdateSession': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateSession,
          request_deserializer=garuda__pb2.Session.FromString,
          response_serializer=garuda__pb2.Void.SerializeToString,
      ),
      'ReadSession': grpc.unary_unary_rpc_method_handler(
          servicer.ReadSession,
          request_deserializer=garuda__pb2.ID.FromString,
          response_serializer=garuda__pb2.Session.SerializeToString,
      ),
      'CreateSession': grpc.unary_unary_rpc_method_handler(
          servicer.CreateSession,
          request_deserializer=garuda__pb2.Session.FromString,
          response_serializer=garuda__pb2.Session.SerializeToString,
      ),
      'ReadSessionsFilter': grpc.unary_stream_rpc_method_handler(
          servicer.ReadSessionsFilter,
          request_deserializer=garuda__pb2.Void.FromString,
          response_serializer=garuda__pb2.Session.SerializeToString,
      ),
      'DeleteArticle': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteArticle,
          request_deserializer=garuda__pb2.ID.FromString,
          response_serializer=garuda__pb2.Void.SerializeToString,
      ),
      'UpdateArticle': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateArticle,
          request_deserializer=garuda__pb2.Article.FromString,
          response_serializer=garuda__pb2.Void.SerializeToString,
      ),
      'ReadArticle': grpc.unary_unary_rpc_method_handler(
          servicer.ReadArticle,
          request_deserializer=garuda__pb2.ID.FromString,
          response_serializer=garuda__pb2.Article.SerializeToString,
      ),
      'CreateArticle': grpc.unary_unary_rpc_method_handler(
          servicer.CreateArticle,
          request_deserializer=garuda__pb2.Article.FromString,
          response_serializer=garuda__pb2.Article.SerializeToString,
      ),
      'ReadArticlesFilter': grpc.unary_stream_rpc_method_handler(
          servicer.ReadArticlesFilter,
          request_deserializer=garuda__pb2.Void.FromString,
          response_serializer=garuda__pb2.Article.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'garuda.Garuda', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
