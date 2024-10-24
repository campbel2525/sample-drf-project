import { NextRequest, NextResponse } from 'next/server'

import { authenticatedClient, errorResponse } from '@/utils/backend-client'

export async function GET(
  request: NextRequest,
  { params }: { params: { id: string } }
) {
  try {
    const response = await authenticatedClient('GET', `/api/v1/users/${params.id}/`)
    const data = await response.json()
    return NextResponse.json(data, {
      status: response.status,
    })
  } catch (error) {
    return errorResponse('API request failed', 500)
  }
}

export async function PUT(
  request: NextRequest,
  { params }: { params: { id: string } }
) {
  try {
    const body = await request.json()
    const response = await authenticatedClient(
      'PUT',
      `/api/v1/users/${params.id}/`,
      null,
      body
    )
    const data = await response.json()
    return NextResponse.json(data, {
      status: response.status,
    })
  } catch (error) {
    return errorResponse('API request failed', 500)
  }
}

export async function DELETE(
  request: NextRequest,
  { params }: { params: { id: string } }
) {
  try {
    const response = await authenticatedClient('DELETE', `/api/v1/users/${params.id}/`)
    if (!response.ok) {
      const data = await response.json()
      return NextResponse.json(data, {
        status: response.status,
      })
    }

    return NextResponse.json(
      {},
      {
        status: 200,
      }
    )
  } catch (error) {
    return errorResponse('API request failed', 500)
  }
}
