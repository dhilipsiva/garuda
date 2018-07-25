// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var garuda_pb = require('./garuda_pb.js');

function serialize_garuda_Article(arg) {
  if (!(arg instanceof garuda_pb.Article)) {
    throw new Error('Expected argument of type garuda.Article');
  }
  return new Buffer(arg.serializeBinary());
}

function deserialize_garuda_Article(buffer_arg) {
  return garuda_pb.Article.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_garuda_ContentType(arg) {
  if (!(arg instanceof garuda_pb.ContentType)) {
    throw new Error('Expected argument of type garuda.ContentType');
  }
  return new Buffer(arg.serializeBinary());
}

function deserialize_garuda_ContentType(buffer_arg) {
  return garuda_pb.ContentType.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_garuda_Group(arg) {
  if (!(arg instanceof garuda_pb.Group)) {
    throw new Error('Expected argument of type garuda.Group');
  }
  return new Buffer(arg.serializeBinary());
}

function deserialize_garuda_Group(buffer_arg) {
  return garuda_pb.Group.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_garuda_ID(arg) {
  if (!(arg instanceof garuda_pb.ID)) {
    throw new Error('Expected argument of type garuda.ID');
  }
  return new Buffer(arg.serializeBinary());
}

function deserialize_garuda_ID(buffer_arg) {
  return garuda_pb.ID.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_garuda_LogEntry(arg) {
  if (!(arg instanceof garuda_pb.LogEntry)) {
    throw new Error('Expected argument of type garuda.LogEntry');
  }
  return new Buffer(arg.serializeBinary());
}

function deserialize_garuda_LogEntry(buffer_arg) {
  return garuda_pb.LogEntry.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_garuda_Permission(arg) {
  if (!(arg instanceof garuda_pb.Permission)) {
    throw new Error('Expected argument of type garuda.Permission');
  }
  return new Buffer(arg.serializeBinary());
}

function deserialize_garuda_Permission(buffer_arg) {
  return garuda_pb.Permission.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_garuda_Session(arg) {
  if (!(arg instanceof garuda_pb.Session)) {
    throw new Error('Expected argument of type garuda.Session');
  }
  return new Buffer(arg.serializeBinary());
}

function deserialize_garuda_Session(buffer_arg) {
  return garuda_pb.Session.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_garuda_User(arg) {
  if (!(arg instanceof garuda_pb.User)) {
    throw new Error('Expected argument of type garuda.User');
  }
  return new Buffer(arg.serializeBinary());
}

function deserialize_garuda_User(buffer_arg) {
  return garuda_pb.User.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_garuda_Void(arg) {
  if (!(arg instanceof garuda_pb.Void)) {
    throw new Error('Expected argument of type garuda.Void');
  }
  return new Buffer(arg.serializeBinary());
}

function deserialize_garuda_Void(buffer_arg) {
  return garuda_pb.Void.deserializeBinary(new Uint8Array(buffer_arg));
}


var GarudaService = exports.GarudaService = {
  deleteLogEntry: {
    path: '/garuda.Garuda/DeleteLogEntry',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.ID,
    responseType: garuda_pb.Void,
    requestSerialize: serialize_garuda_ID,
    requestDeserialize: deserialize_garuda_ID,
    responseSerialize: serialize_garuda_Void,
    responseDeserialize: deserialize_garuda_Void,
  },
  updateLogEntry: {
    path: '/garuda.Garuda/UpdateLogEntry',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.LogEntry,
    responseType: garuda_pb.Void,
    requestSerialize: serialize_garuda_LogEntry,
    requestDeserialize: deserialize_garuda_LogEntry,
    responseSerialize: serialize_garuda_Void,
    responseDeserialize: deserialize_garuda_Void,
  },
  readLogEntry: {
    path: '/garuda.Garuda/ReadLogEntry',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.ID,
    responseType: garuda_pb.LogEntry,
    requestSerialize: serialize_garuda_ID,
    requestDeserialize: deserialize_garuda_ID,
    responseSerialize: serialize_garuda_LogEntry,
    responseDeserialize: deserialize_garuda_LogEntry,
  },
  createLogEntry: {
    path: '/garuda.Garuda/CreateLogEntry',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.LogEntry,
    responseType: garuda_pb.LogEntry,
    requestSerialize: serialize_garuda_LogEntry,
    requestDeserialize: deserialize_garuda_LogEntry,
    responseSerialize: serialize_garuda_LogEntry,
    responseDeserialize: deserialize_garuda_LogEntry,
  },
  readLogEntrysFilter: {
    path: '/garuda.Garuda/ReadLogEntrysFilter',
    requestStream: false,
    responseStream: true,
    requestType: garuda_pb.Void,
    responseType: garuda_pb.LogEntry,
    requestSerialize: serialize_garuda_Void,
    requestDeserialize: deserialize_garuda_Void,
    responseSerialize: serialize_garuda_LogEntry,
    responseDeserialize: deserialize_garuda_LogEntry,
  },
  deletePermission: {
    path: '/garuda.Garuda/DeletePermission',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.ID,
    responseType: garuda_pb.Void,
    requestSerialize: serialize_garuda_ID,
    requestDeserialize: deserialize_garuda_ID,
    responseSerialize: serialize_garuda_Void,
    responseDeserialize: deserialize_garuda_Void,
  },
  updatePermission: {
    path: '/garuda.Garuda/UpdatePermission',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.Permission,
    responseType: garuda_pb.Void,
    requestSerialize: serialize_garuda_Permission,
    requestDeserialize: deserialize_garuda_Permission,
    responseSerialize: serialize_garuda_Void,
    responseDeserialize: deserialize_garuda_Void,
  },
  readPermission: {
    path: '/garuda.Garuda/ReadPermission',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.ID,
    responseType: garuda_pb.Permission,
    requestSerialize: serialize_garuda_ID,
    requestDeserialize: deserialize_garuda_ID,
    responseSerialize: serialize_garuda_Permission,
    responseDeserialize: deserialize_garuda_Permission,
  },
  createPermission: {
    path: '/garuda.Garuda/CreatePermission',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.Permission,
    responseType: garuda_pb.Permission,
    requestSerialize: serialize_garuda_Permission,
    requestDeserialize: deserialize_garuda_Permission,
    responseSerialize: serialize_garuda_Permission,
    responseDeserialize: deserialize_garuda_Permission,
  },
  readPermissionsFilter: {
    path: '/garuda.Garuda/ReadPermissionsFilter',
    requestStream: false,
    responseStream: true,
    requestType: garuda_pb.Void,
    responseType: garuda_pb.Permission,
    requestSerialize: serialize_garuda_Void,
    requestDeserialize: deserialize_garuda_Void,
    responseSerialize: serialize_garuda_Permission,
    responseDeserialize: deserialize_garuda_Permission,
  },
  deleteGroup: {
    path: '/garuda.Garuda/DeleteGroup',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.ID,
    responseType: garuda_pb.Void,
    requestSerialize: serialize_garuda_ID,
    requestDeserialize: deserialize_garuda_ID,
    responseSerialize: serialize_garuda_Void,
    responseDeserialize: deserialize_garuda_Void,
  },
  updateGroup: {
    path: '/garuda.Garuda/UpdateGroup',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.Group,
    responseType: garuda_pb.Void,
    requestSerialize: serialize_garuda_Group,
    requestDeserialize: deserialize_garuda_Group,
    responseSerialize: serialize_garuda_Void,
    responseDeserialize: deserialize_garuda_Void,
  },
  readGroup: {
    path: '/garuda.Garuda/ReadGroup',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.ID,
    responseType: garuda_pb.Group,
    requestSerialize: serialize_garuda_ID,
    requestDeserialize: deserialize_garuda_ID,
    responseSerialize: serialize_garuda_Group,
    responseDeserialize: deserialize_garuda_Group,
  },
  createGroup: {
    path: '/garuda.Garuda/CreateGroup',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.Group,
    responseType: garuda_pb.Group,
    requestSerialize: serialize_garuda_Group,
    requestDeserialize: deserialize_garuda_Group,
    responseSerialize: serialize_garuda_Group,
    responseDeserialize: deserialize_garuda_Group,
  },
  readGroupsFilter: {
    path: '/garuda.Garuda/ReadGroupsFilter',
    requestStream: false,
    responseStream: true,
    requestType: garuda_pb.Void,
    responseType: garuda_pb.Group,
    requestSerialize: serialize_garuda_Void,
    requestDeserialize: deserialize_garuda_Void,
    responseSerialize: serialize_garuda_Group,
    responseDeserialize: deserialize_garuda_Group,
  },
  deleteUser: {
    path: '/garuda.Garuda/DeleteUser',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.ID,
    responseType: garuda_pb.Void,
    requestSerialize: serialize_garuda_ID,
    requestDeserialize: deserialize_garuda_ID,
    responseSerialize: serialize_garuda_Void,
    responseDeserialize: deserialize_garuda_Void,
  },
  updateUser: {
    path: '/garuda.Garuda/UpdateUser',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.User,
    responseType: garuda_pb.Void,
    requestSerialize: serialize_garuda_User,
    requestDeserialize: deserialize_garuda_User,
    responseSerialize: serialize_garuda_Void,
    responseDeserialize: deserialize_garuda_Void,
  },
  readUser: {
    path: '/garuda.Garuda/ReadUser',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.ID,
    responseType: garuda_pb.User,
    requestSerialize: serialize_garuda_ID,
    requestDeserialize: deserialize_garuda_ID,
    responseSerialize: serialize_garuda_User,
    responseDeserialize: deserialize_garuda_User,
  },
  createUser: {
    path: '/garuda.Garuda/CreateUser',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.User,
    responseType: garuda_pb.User,
    requestSerialize: serialize_garuda_User,
    requestDeserialize: deserialize_garuda_User,
    responseSerialize: serialize_garuda_User,
    responseDeserialize: deserialize_garuda_User,
  },
  readUsersFilter: {
    path: '/garuda.Garuda/ReadUsersFilter',
    requestStream: false,
    responseStream: true,
    requestType: garuda_pb.Void,
    responseType: garuda_pb.User,
    requestSerialize: serialize_garuda_Void,
    requestDeserialize: deserialize_garuda_Void,
    responseSerialize: serialize_garuda_User,
    responseDeserialize: deserialize_garuda_User,
  },
  deleteContentType: {
    path: '/garuda.Garuda/DeleteContentType',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.ID,
    responseType: garuda_pb.Void,
    requestSerialize: serialize_garuda_ID,
    requestDeserialize: deserialize_garuda_ID,
    responseSerialize: serialize_garuda_Void,
    responseDeserialize: deserialize_garuda_Void,
  },
  updateContentType: {
    path: '/garuda.Garuda/UpdateContentType',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.ContentType,
    responseType: garuda_pb.Void,
    requestSerialize: serialize_garuda_ContentType,
    requestDeserialize: deserialize_garuda_ContentType,
    responseSerialize: serialize_garuda_Void,
    responseDeserialize: deserialize_garuda_Void,
  },
  readContentType: {
    path: '/garuda.Garuda/ReadContentType',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.ID,
    responseType: garuda_pb.ContentType,
    requestSerialize: serialize_garuda_ID,
    requestDeserialize: deserialize_garuda_ID,
    responseSerialize: serialize_garuda_ContentType,
    responseDeserialize: deserialize_garuda_ContentType,
  },
  createContentType: {
    path: '/garuda.Garuda/CreateContentType',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.ContentType,
    responseType: garuda_pb.ContentType,
    requestSerialize: serialize_garuda_ContentType,
    requestDeserialize: deserialize_garuda_ContentType,
    responseSerialize: serialize_garuda_ContentType,
    responseDeserialize: deserialize_garuda_ContentType,
  },
  readContentTypesFilter: {
    path: '/garuda.Garuda/ReadContentTypesFilter',
    requestStream: false,
    responseStream: true,
    requestType: garuda_pb.Void,
    responseType: garuda_pb.ContentType,
    requestSerialize: serialize_garuda_Void,
    requestDeserialize: deserialize_garuda_Void,
    responseSerialize: serialize_garuda_ContentType,
    responseDeserialize: deserialize_garuda_ContentType,
  },
  deleteSession: {
    path: '/garuda.Garuda/DeleteSession',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.ID,
    responseType: garuda_pb.Void,
    requestSerialize: serialize_garuda_ID,
    requestDeserialize: deserialize_garuda_ID,
    responseSerialize: serialize_garuda_Void,
    responseDeserialize: deserialize_garuda_Void,
  },
  updateSession: {
    path: '/garuda.Garuda/UpdateSession',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.Session,
    responseType: garuda_pb.Void,
    requestSerialize: serialize_garuda_Session,
    requestDeserialize: deserialize_garuda_Session,
    responseSerialize: serialize_garuda_Void,
    responseDeserialize: deserialize_garuda_Void,
  },
  readSession: {
    path: '/garuda.Garuda/ReadSession',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.ID,
    responseType: garuda_pb.Session,
    requestSerialize: serialize_garuda_ID,
    requestDeserialize: deserialize_garuda_ID,
    responseSerialize: serialize_garuda_Session,
    responseDeserialize: deserialize_garuda_Session,
  },
  createSession: {
    path: '/garuda.Garuda/CreateSession',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.Session,
    responseType: garuda_pb.Session,
    requestSerialize: serialize_garuda_Session,
    requestDeserialize: deserialize_garuda_Session,
    responseSerialize: serialize_garuda_Session,
    responseDeserialize: deserialize_garuda_Session,
  },
  readSessionsFilter: {
    path: '/garuda.Garuda/ReadSessionsFilter',
    requestStream: false,
    responseStream: true,
    requestType: garuda_pb.Void,
    responseType: garuda_pb.Session,
    requestSerialize: serialize_garuda_Void,
    requestDeserialize: deserialize_garuda_Void,
    responseSerialize: serialize_garuda_Session,
    responseDeserialize: deserialize_garuda_Session,
  },
  deleteArticle: {
    path: '/garuda.Garuda/DeleteArticle',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.ID,
    responseType: garuda_pb.Void,
    requestSerialize: serialize_garuda_ID,
    requestDeserialize: deserialize_garuda_ID,
    responseSerialize: serialize_garuda_Void,
    responseDeserialize: deserialize_garuda_Void,
  },
  updateArticle: {
    path: '/garuda.Garuda/UpdateArticle',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.Article,
    responseType: garuda_pb.Void,
    requestSerialize: serialize_garuda_Article,
    requestDeserialize: deserialize_garuda_Article,
    responseSerialize: serialize_garuda_Void,
    responseDeserialize: deserialize_garuda_Void,
  },
  readArticle: {
    path: '/garuda.Garuda/ReadArticle',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.ID,
    responseType: garuda_pb.Article,
    requestSerialize: serialize_garuda_ID,
    requestDeserialize: deserialize_garuda_ID,
    responseSerialize: serialize_garuda_Article,
    responseDeserialize: deserialize_garuda_Article,
  },
  createArticle: {
    path: '/garuda.Garuda/CreateArticle',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.Article,
    responseType: garuda_pb.Article,
    requestSerialize: serialize_garuda_Article,
    requestDeserialize: deserialize_garuda_Article,
    responseSerialize: serialize_garuda_Article,
    responseDeserialize: deserialize_garuda_Article,
  },
  readArticlesFilter: {
    path: '/garuda.Garuda/ReadArticlesFilter',
    requestStream: false,
    responseStream: true,
    requestType: garuda_pb.Void,
    responseType: garuda_pb.Article,
    requestSerialize: serialize_garuda_Void,
    requestDeserialize: deserialize_garuda_Void,
    responseSerialize: serialize_garuda_Article,
    responseDeserialize: deserialize_garuda_Article,
  },
  customCallDemo: {
    path: '/garuda.Garuda/CustomCallDemo',
    requestStream: false,
    responseStream: false,
    requestType: garuda_pb.Void,
    responseType: garuda_pb.Void,
    requestSerialize: serialize_garuda_Void,
    requestDeserialize: deserialize_garuda_Void,
    responseSerialize: serialize_garuda_Void,
    responseDeserialize: deserialize_garuda_Void,
  },
};

exports.GarudaClient = grpc.makeGenericClientConstructor(GarudaService);
