export const startCase = (str: string) =>
  str
    .replace("-", " ")
    .replace(/(?:^|\s|["'([{])+\S/g, (match) => match.toUpperCase());
