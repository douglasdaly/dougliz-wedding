// api/index.ts

// Simple Guest Auth
const DUMMY_PROMPT = 'In what city did Doug & Liz meet?'
const DUMMY_CODES = ['nyc', 'new york', 'new york city']

export const getAllowed = async (): Promise<boolean> => {
  const data = await new Promise<boolean>(resolve =>
    setTimeout(() => resolve(false))
  )
  return data
}

export const getPasscodePrompt = async (): Promise<string> => {
  const data = await new Promise<string>(resolve =>
    setTimeout(() => resolve(DUMMY_PROMPT))
  )
  return data
}

export const checkPasscode = async (passcode: string): Promise<boolean> => {
  const fmtPass = passcode.trim().toLowerCase()
  if (fmtPass) {
    const isValid = await new Promise<boolean>(resolve =>
      setTimeout(() => resolve(DUMMY_CODES.includes(fmtPass)))
    )
    return isValid
  }
  return false
}
