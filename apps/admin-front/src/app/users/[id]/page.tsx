import { Box } from '@chakra-ui/react'

import NotFound from '@/components/common/NotFound'
import ServerError from '@/components/common/ServerError'
import UserRetrieveComponent from '@/components/fetch/UserRetrieveComponent'
import ErrorMessage from '@/components/messages/ErrorMessage'
import ValidationErrorMessages from '@/components/messages/ValidationErrorMessages'
import { fetchClient } from '@/utils/backend-client'

export default async function UserRetrievePage({ params }: { params: { id: string } }) {
  const { id } = params

  let validationError = {}
  let errorMessage = ''

  const response = await fetchClient('GET', `/api/users/${id}/`)
  const responseData = await response.json()
  if (!response.ok) {
    if (response.status === 400) {
      validationError = responseData
    }
    if (response.status === 404) {
      return <NotFound />
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
      {responseData && <UserRetrieveComponent user={responseData} />}

      <Box p={8} maxWidth="400px">
        {Object.keys(validationError).length > 0 && (
          <ValidationErrorMessages validationError={validationError} />
        )}
        {errorMessage && <ErrorMessage message={errorMessage} />}
      </Box>
    </>
  )
}
