import { cookies } from 'next/headers'
import { NextResponse } from 'next/server'

import { ACCESS_TOKEN_NAME, REFRESH_TOKEN_NAME } from '@/config/settings'
import { errorResponse } from '@/utils/backend-client'

export async function POST(): Promise<NextResponse> {
  try {
    // クッキーからjwtを削除
    cookies().set({
      name: ACCESS_TOKEN_NAME,
      value: '',
      httpOnly: true,
      secure: true,
      maxAge: 0,
    })
    cookies().set({
      name: REFRESH_TOKEN_NAME,
      value: '',
      httpOnly: true,
      secure: true,
      maxAge: 0,
    })

    return NextResponse.json({}, { status: 200 })
  } catch (error) {
    return errorResponse('API request failed', 500)
  }
}
