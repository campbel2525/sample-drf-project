import { NextRequest, NextResponse } from 'next/server'

import { authenticatedClient, errorResponse } from '@/utils/backend-client'
import { checkCsrfToken } from '@/utils/csrf-token'

export async function POST(request: NextRequest): Promise<NextResponse> {
  try {
    checkCsrfToken(request)

    const body = await request.json()
    const response = await authenticatedClient(
      'POST',
      `/api/v1/accounts/reset-password/confirm/`,
      null,
      body
    )

    if (response.status === 204) {
      return new NextResponse(null, {
        status: 204,
      })
    }

    const data = await response.json()
    return NextResponse.json(data, {
      status: response.status,
    })
  } catch (error) {
    const errorMessage = error instanceof Error ? error.message : String(error)
    return errorResponse(errorMessage as string, 500)
  }
}