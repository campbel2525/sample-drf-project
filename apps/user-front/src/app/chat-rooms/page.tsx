'use client'

import { Box, SimpleGrid } from '@chakra-ui/react'
import { useRouter } from 'next/navigation'
import React, { useEffect, useState } from 'react'

import { chatRoomIndexApi } from '@/api/chat-room-api'
import Loading from '@/components/Loading'
import ErrorMessage from '@/components/messages/ErrorMessage'
import ValidationErrorMessages from '@/components/messages/ValidationErrorMessages'
import { frontPaths } from '@/config/settings'
import type { ApiResponse } from '@/types/responses/base-responses'
import type { validationErrorDetail } from '@/types/responses/base-responses'
import type { ChatRoomIndexResponse } from '@/types/responses/chat-responses'
import { loginCheck } from '@/utils/auth'

export default function ChatRoomIndexPage() {
  const router = useRouter()
  const [errorMessage, setErrorMessage] = useState<string>('')
  const [validationErrors, setValidationErrors] = useState<validationErrorDetail[]>([])
  const [result, setResult] = useState<ApiResponse<ChatRoomIndexResponse>>()

  const fetchData = async () => {
    const result: ApiResponse<ChatRoomIndexResponse> = await chatRoomIndexApi()
    setValidationErrors(result.validationErrors ?? [])
    setErrorMessage(result.errorMessage || '')
    setResult(result)
  }
  useEffect(() => {
    const performAsyncOperations = async () => {
      await loginCheck(router)
      await fetchData()
    }

    performAsyncOperations()
  }, [router])

  if (!result) {
    return <Loading />
  }

  return (
    <>
      {result?.data?.data && (
        <Box padding="4" width="full" maxWidth="1200px" mx="auto">
          <SimpleGrid columns={{ base: 2, md: 3, lg: 4, xl: 5 }} spacing="4">
            {result.data.data.map((chat_room) => (
              <Box
                key={chat_room.uuid}
                p="5"
                shadow="md"
                borderWidth="1px"
                onClick={() =>
                  router.push(`${frontPaths.chatMessages}/${chat_room.id}`)
                }
              >
                <p>{chat_room.name}</p>
              </Box>
            ))}
          </SimpleGrid>
        </Box>
      )}

      <Box p={8} maxWidth="400px">
        {validationErrors.length > 0 && (
          <ValidationErrorMessages validationErrors={validationErrors} />
        )}
        {errorMessage && <ErrorMessage message={errorMessage} />}
      </Box>
    </>
  )
}
