import type { ChatRoom, ChatMessage } from '@/types/models'

// chat-rooms
export type ChatRoomIndexResponse = {
  data: ChatRoom[]
}

// chat-room-messages
export type ChatRoomMessageIndexResponse = {
  data: ChatMessage[]
}
