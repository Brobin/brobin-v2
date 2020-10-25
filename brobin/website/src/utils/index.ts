export const startCase = (str: string): string =>
  str
    .replace("-", " ")
    .replace(/(?:^|\s|["'([{])+\S/g, (match) => match.toUpperCase());

export default {
  startCase,
};
