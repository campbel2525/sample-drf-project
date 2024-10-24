export const localStorageKeys = {
  accessToken: 'access_token',
  refreshToken: 'refresh_token',
}

export const frontPaths = {
  home: '/',
  login: '/accounts/login',
  signUp: '/accounts/signup',
  users: '/users',
  chatRooms: '/chat-rooms',
  chatMessages: '/chat-messages',
}

export const loginPagePath = frontPaths.login

export const ACCESS_TOKEN_NAME = 'access_token'
export const REFRESH_TOKEN_NAME = 'refresh_token'
export const ACCESS_TOKEN_UPDATE_BUFFER = 60 * 60 * 24 // 1日

// 認証が必要ないパス
export const authNotRequiredPaths = ['/accounts/login', '/accounts/signup']
