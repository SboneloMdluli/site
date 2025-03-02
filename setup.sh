# Install Go (required for Hugo modules)
if ! command -v go &> /dev/null; then
    echo "Installing Go..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        brew install go
    else
        # Ubuntu/Debian
        sudo apt-get update
        sudo apt-get install -y golang-go
    fi
fi

# Install Hugo (if not already installed)
if ! command -v hugo &> /dev/null; then
    echo "Installing Hugo..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        brew install hugo
    else
        # Ubuntu/Debian
        sudo apt-get install -y hugo
    fi
fi

# Create new site
hugo new site notebook-blog
cd notebook-blog

# Add Hugo Blox Builder theme
git init
git submodule add https://github.com/HugoBlox/hugo-blox-builder.git themes/hugo-blox-builder

# Initialize Hugo modules
go mod init github.com/YOUR_USERNAME/REPO_NAME
hugo mod get github.com/HugoBlox/hugo-blox-builder/modules/blox-bootstrap/v5@latest
hugo mod get github.com/HugoBlox/hugo-blox-builder/modules/blox-core@latest
hugo mod get github.com/HugoBlox/hugo-blox-builder/modules/blox-seo@latest
hugo mod tidy