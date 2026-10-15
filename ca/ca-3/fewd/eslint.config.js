import eslintRecommended from '@eslint/js';

export default [
  {
    files: ['**/*.js', '**/*.mjs'],
    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module',
    },
    rules: {
      ...eslintRecommended.configs.recommended.rules,
      'no-undef': 'warn',
      // Disallow use of execution blocking keywords
      'no-restricted-globals': [
        'error',
        { name: 'alert', message: 'Avoid using alert.' },
        { name: 'confirm', message: 'Avoid using confirm.' },
        { name: 'prompt', message: 'Avoid using prompt.' },
      ],
      // Enable unused variables detection
      'no-unused-vars': [
        'warn',
        {
          vars: 'all',
          varsIgnorePattern: '^_',
          args: 'after-used',
          argsIgnorePattern: '^_',
        },
      ],
    },
  },
  {
    ignores: [
      'dist', // Ignore build files
      '**/*.spec.js', // Ignore test files with .spec.js extension
      '**/*.test.js', // Ignore test files with .test.js extension
      '**/FunctionsTest.js', // Ignore specific test file
      '*.lock', // Ignore lock files
      'package-lock.json', // Ignore npm lock file
      'jasmine/**', // Ignore all files in the jasmine directory
    ],
  },
];
