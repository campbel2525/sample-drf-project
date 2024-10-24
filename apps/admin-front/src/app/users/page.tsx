import { Box } from '@chakra-ui/react'

import ServerError from '@/components/common/ServerError'
import UserListComponent from '@/components/fetch/UserListComponent'
import ErrorMessage from '@/components/messages/ErrorMessage'
import ValidationErrorMessages from '@/components/messages/ValidationErrorMessages'
import { fetchClient } from '@/utils/backend-client'

export default async function UserIndexPage() {
  let validationError = {}
  let errorMessage = ''

  const response = await fetchClient('GET', '/api/users/')
  const responseData = await response.json()
  if (!response.ok) {
    if (response.status === 400) {
      validationError = responseData
    }
    if (response.status === 500) {
      return <ServerError />
    }
    if (responseData?.detail) {
      errorMessage = responseData.detail
    }
  }

  return (
    <>
      {responseData.data && (
        <Box padding="4" width="full" maxWidth="1200px" mx="auto">
          {/* データをクライアントコンポーネントに渡す */}
          <UserListComponent users={responseData.data} />
        </Box>
      )}

      <Box p={8} maxWidth="400px">
        {Object.keys(validationError).length > 0 && (
          <ValidationErrorMessages validationError={validationError} />
        )}
        {errorMessage && <ErrorMessage message={errorMessage} />}
      </Box>
    </>
  )
}
