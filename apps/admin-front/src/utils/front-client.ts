// APIリクエスト
export const client = async (
  method: string,
  path: string,
  queryParams: null | Record<string, string> = null,
  body: null | Record<string, string | number | boolean | null> = null,
  accessToken: string = ''
): Promise<Response> => {
  // クエリパラメータをURLに追加
  let url = path
  if (queryParams && Object.keys(queryParams).length > 0) {
    url += `?${new URLSearchParams(queryParams).toString()}`
  }

  // ヘッダーを設定
  const headers: Record<string, string> = {}

  if (accessToken) {
    headers.Cookie = `access_token=${accessToken}`
  }

  if (body && Object.keys(body).length > 0) {
    headers['Content-Type'] = 'application/json' as string
  }

  // リクエスト
  const response = await fetch(url, {
    method: method,
    headers: headers,
    body: body ? JSON.stringify(body) : undefined,
    cache: 'no-store',
    credentials: 'include',
  })

  return response
}
