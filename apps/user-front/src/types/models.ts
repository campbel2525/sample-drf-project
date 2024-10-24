export type User = {
  id: number
  email: string
  is_active: boolean
  name: string
  created_at: string
  updated_at: string
}

export type ChatRoom = {
  uuid: string
  name: string
  last_message_at: string
  created_at: string
  updated_at: string
}

export type ChatMessage = {
  message: string
  message_token: number
  role: string
  ai_model_name: string
  ai_model_version: string
  ai_model_provider: string
  created_at: string
  updated_at: string
}
