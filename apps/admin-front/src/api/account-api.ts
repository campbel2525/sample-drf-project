import request from '@/api/base-api'
import { localStorageKeys } from '@/config/settings'
import type { AdminUser } from '@/types/models'
import type { LoginRequest } from '@/types/requests/account-requests'
import type { TokenResponse } from '@/types/responses/account-responses'
import type { ApiResponse } from '@/types/responses/base-responses'

export const loginApi = async (
  data: LoginRequest
): Promise<ApiResponse<TokenResponse>> => {
  try {
    const result = await request({
      url: `/api/v1/accounts/login/`,
      method: 'post',
      data: data,
    })
    return result.data
  } catch (error) {
    return Promise.reject({
      message: 'API request failed',
      error: error,
    })
  }
}

export const meApi = async (): Promise<ApiResponse<AdminUser>> => {
  try {
    const result = await request({
      url: `/api/v1/accounts/me/`,
      method: 'get',
    })
    return result.data
  } catch (error) {
    return Promise.reject({
      message: 'API request failed',
      error: error,
    })
  }
}

export const refreshTokenApi = async (): Promise<ApiResponse<TokenResponse>> => {
  try {
    const refreshToken = localStorage.getItem(localStorageKeys.refreshToken)
    const result = await request({
      url: `/api/v1/accounts/refresh-token/`,
      method: 'post',
      data: {
        refresh_token: refreshToken,
      },
    })
    return result.data
  } catch (error) {
    return Promise.reject({
      message: 'API request failed',
      error: error,
    })
  }
}
