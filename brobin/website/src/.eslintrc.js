module.exports = {
  env: {
    mocha: true,
    node: true
  },
  extends: ['airbnb-base', 'prettier', 'plugin:prettier/recommended'],
  plugins: ['prettier'],
  rules: {
    'class-methods-use-this': 0,
    // don't allow dangling commas
    'comma-dangle': [2, 'never'],
    // allow windows CRLF locally to windows (git converts back to unix LF on push)
    'linebreak-style': ['error', require('os').EOL === '\r\n' ? 'windows' : 'unix'],
    'import/no-extraneous-dependencies': ['error', { devDependencies: true }],
    'prettier/prettier': ['error']
  },
  globals: {
    expect: true,
    should: true
  },
  settings: {
    'import/resolver': {
      node: {
        extensions: ['.js', '.tsx', '.json']
      }
    }
  },
  overrides: [
    {
      files: ['**/*.tsx'],
      env: {
        mocha: true,
        node: true
      },
      parser: '@typescript-eslint/parser',
      parserOptions: {
        project: './tsconfig.eslint.json'
      },
      extends: [
        'airbnb-base',
        'plugin:@typescript-eslint/recommended',
        'plugin:@typescript-eslint/recommended-requiring-type-checking',
        'plugin:prettier/recommended',
        'plugin:import/typescript',
        'prettier/@typescript-eslint'
      ],
      plugins: ['@typescript-eslint'],
      rules: {
        'class-methods-use-this': 0,
        // don't allow dangling commas
        'comma-dangle': [2, 'never'],
        // allow windows CRLF locally to windows (git converts back to unix LF on push)
        'linebreak-style': ['error', require('os').EOL === '\r\n' ? 'windows' : 'unix'],
        'import/no-extraneous-dependencies': ['error', { devDependencies: true }],
        'lines-between-class-members': ['error', 'always', { exceptAfterSingleLine: true }]
      },
      settings: {
        'import/parsers': {
          '@typescript-eslint/parser': ['.ts']
        }
      },
      globals: {
        expect: true,
        should: true
      }
    }
  ]
};