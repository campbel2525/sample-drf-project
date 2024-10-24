import { NextRequest, NextResponse } from 'next/server'

import { ACCESS_TOKEN_NAME, REFRESH_TOKEN_NAME } from '@/config/settings'
import { unauthenticatedClient, errorResponse } from '@/utils/backend-client'
import { setTokenCookie } from '@/utils/jwt'

export async function POST(request: NextRequest): Promise<NextResponse> {
  try {
    const body = await request.json()
    const response = await unauthenticatedClient(
      'POST',
      '/api/v1/accounts/signup/',
      null,
      body
    )

    const data = await response.json()
    if (response.status !== 200) {
      return NextResponse.json(data, {
        status: response.status,
      })
    }

    const apiResponse = NextResponse.json(data, {
      status: response.status,
    })
    setTokenCookie(ACCESS_TOKEN_NAME, data.access_token)
    setTokenCookie(REFRESH_TOKEN_NAME, data.refresh_token)
    return apiResponse
  } catch (error) {
    return errorResponse('API request failed', 500)
  }
}
