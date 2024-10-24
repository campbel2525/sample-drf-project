import { NextResponse } from 'next/server'

import { authenticatedClient, errorResponse } from '@/utils/backend-client'

export async function GET(): Promise<NextResponse> {
  try {
    const response = await authenticatedClient('GET', '/api/v1/accounts/me/')

    const data = await response.json()
    return NextResponse.json(data, {
      status: response.status,
    })
  } catch (error) {
    return errorResponse('API request failed', 500)
  }
}
