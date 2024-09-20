// Helper functions for the UI

/**
 * Formats a date string into a more readable format
 * @param dateString - The date string to format
 * @returns A formatted date string
 */
export const formatDate = (dateString: string): string => {
  const options: Intl.DateTimeFormatOptions = { 
    year: 'numeric', 
    month: 'short', 
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  };
  return new Date(dateString).toLocaleDateString(undefined, options);
};

/**
 * Truncates a string to a specified length and adds an ellipsis
 * @param str - The string to truncate
 * @param maxLength - The maximum length of the string
 * @returns The truncated string
 */
export const truncateString = (str: string, maxLength: number): string => {
  if (str.length <= maxLength) return str;
  return str.slice(0, maxLength - 3) + '...';
};

/**
 * Generates a random color in hexadecimal format
 * @returns A random color as a hex string
 */
export const generateRandomColor = (): string => {
  return '#' + Math.floor(Math.random()*16777215).toString(16);
};

// Add more helper functions as needed
