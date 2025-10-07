{
  description = "Python monorepo with UV workspace";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            # Python
            python311

            # UV - Python package manager
            uv

            # Development tools
            git

            # Additional useful tools
            jq
            curl

            # For better shell experience
            direnv
          ];

          shellHook = ''
            echo "🐍 Python Monorepo Development Environment"
            echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            echo ""
            echo "Available commands:"
            echo "  uv sync              - Install all dependencies"
            echo "  uv run pytest        - Run all tests"
            echo "  uv run ruff check    - Lint code"
            echo "  uv run ruff format   - Format code"
            echo "  uv run mypy .        - Type check code"
            echo ""
            echo "Workspace structure:"
            echo "  packages/python/     - Shared libraries"
            echo "  services/python/     - Services"
            echo ""
            echo "Python version: $(python --version)"
            echo "UV version: $(uv --version)"
            echo ""
          '';
        };

        # Optional: Define packages for building
        packages = {
          # You can add package builds here if needed
        };
      }
    );
}
