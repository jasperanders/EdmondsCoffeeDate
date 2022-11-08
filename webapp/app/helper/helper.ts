/**
 * This function creates a nested array from a string.
 * Input:
 *
 * Alice
 * Bob
 * Peter
 *
 * Jordan
 * Dan
 * Fred
 *
 * Output: [[Alice, Bob, Peter], [Jordan, Dan, Fred]]
 */
export function createNestedArrayFromString(str: string): string[][] {
  // split string at empty lines
  const splitString = str.split(/\n\s*\n/);
  // for each string in splitString, split at new line
  const result = splitString.map((s) => s.split(/\n/));
  // remove all trailing and leading white spaces in the deep array result
  return result.map((r) => r.map((s) => s.trim()));
}
