function(search_cross_tool SEARCH_DIRECTORY TOOL_NAME TOOL_NAME_REGEX TOOL_USE_STDERR TOOL_VERSION_ARGUMENT TOOL_VERSION_STRING_REGEX TOOL_TARGET_STRING_REGEX TOOL_TARGET_REGEX TOOL_PATH_VARIABLE TOOL_VERSION_VARIABLE)
	if(DEFINED ${TOOL_PATH_VARIABLE})
		if(DEFINED ${TOOL_VERSION_VARIABLE})
			set(TOOL_PATH "${${TOOL_PATH_VARIABLE}}")
			set(TOOL_VERSION "${${TOOL_VERSION_VARIABLE}}")
		endif()
	endif()

	file(GLOB TOOL_CANDIDATE_PATHS "${SEARCH_DIRECTORY}/*${TOOL_NAME}*")
	foreach(TOOL_CANDIDATE_PATH ${TOOL_CANDIDATE_PATHS})
		if("${TOOL_CANDIDATE_PATH}" MATCHES "${TOOL_NAME_REGEX}")
			if("${TOOL_USE_STDERR}")
				execute_process(COMMAND "${TOOL_CANDIDATE_PATH}" "${TOOL_VERSION_ARGUMENT}"
					TIMEOUT 0.1
					RESULT_VARIABLE TOOL_CANDIDATE_RESULT
					ERROR_VARIABLE TOOL_CANDIDATE_OUTPUT
					ERROR_STRIP_TRAILING_WHITESPACE
					OUTPUT_QUIET)
			else()
				execute_process(COMMAND "${TOOL_CANDIDATE_PATH}" "${TOOL_VERSION_ARGUMENT}"
					TIMEOUT 0.1
					RESULT_VARIABLE TOOL_CANDIDATE_RESULT
					OUTPUT_VARIABLE TOOL_CANDIDATE_OUTPUT
					OUTPUT_STRIP_TRAILING_WHITESPACE
					ERROR_QUIET)
			endif()
			if(${TOOL_CANDIDATE_RESULT} EQUAL 0)
				if("${TOOL_CANDIDATE_OUTPUT}" MATCHES "${TOOL_TARGET_STRING_REGEX}")
					string(REGEX REPLACE "${TOOL_TARGET_STRING_REGEX}" "\\1" TOOL_CANDIDATE_TARGET "${TOOL_CANDIDATE_OUTPUT}")
					if("${TOOL_CANDIDATE_TARGET}" MATCHES "${TOOL_TARGET_REGEX}")
						if("${TOOL_CANDIDATE_OUTPUT}" MATCHES "${TOOL_VERSION_STRING_REGEX}")
							string(REGEX REPLACE "${TOOL_VERSION_STRING_REGEX}" "\\1" TOOL_CANDIDATE_VERSION "${TOOL_CANDIDATE_OUTPUT}")
							if((NOT DEFINED TOOL_PATH) OR (NOT DEFINED TOOL_VERSION))
								set(TOOL_VERSION ${TOOL_CANDIDATE_VERSION})
								set(TOOL_PATH "${TOOL_CANDIDATE_PATH}")
							elseif(${TOOL_CANDIDATE_VERSION} VERSION_GREATER ${TOOL_VERSION})
								set(TOOL_VERSION ${TOOL_CANDIDATE_VERSION})
								set(TOOL_PATH "${TOOL_CANDIDATE_PATH}")
							elseif(${TOOL_CANDIDATE_VERSION} VERSION_EQUAL ${TOOL_VERSION})
								get_filename_component(TOOL_FILE_NAME "${TOOL_PATH}" NAME)
								get_filename_component(TOOL_CANDIDATE_FILE_NAME "${TOOL_CANDIDATE_PATH}" NAME)
								string(LENGTH "${TOOL_FILE_NAME}" TOOL_FILE_NAME_LENGTH)
								string(LENGTH "${TOOL_CANDIDATE_FILE_NAME}" TOOL_CANDIDATE_FILE_NAME_LENGTH)
								if(${TOOL_CANDIDATE_FILE_NAME_LENGTH} LESS ${TOOL_FILE_NAME_LENGTH})
									set(TOOL_VERSION ${TOOL_CANDIDATE_VERSION})
									set(TOOL_PATH "${TOOL_CANDIDATE_PATH}")
								endif()
							endif()
						endif()
					endif()
				endif()
			endif()
		endif()
	endforeach(TOOL_CANDIDATE_PATH)
	if(DEFINED TOOL_PATH)
		if(DEFINED TOOL_VERSION)
			set(${TOOL_PATH_VARIABLE} "${TOOL_PATH}" PARENT_SCOPE)
			set(${TOOL_VERSION_VARIABLE} "${TOOL_VERSION}" PARENT_SCOPE)
		endif()
	endif()
endfunction()

function(search_cross_gcc SEARCH_DIRECTORY GCC_NAME GCC_NAME_REGEX GCC_TARGET_REGEX GCC_PATH_VARIABLE GCC_VERSION_VARIABLE)
	set(GCC_VERSION_STRING_REGEX ".*gcc version ([0-9]+([.][0-9]+)+).*")
	set(GCC_TARGET_STRING_REGEX ".*Target: ([A-Za-z0-9\\._]+([-][A-Za-z0-9\\._]+)+).*")
	if(DEFINED ${GCC_PATH_VARIABLE})
		if(DEFINED ${GCC_VERSION_VARIABLE})
			set(GCC_PATH "${${GCC_PATH_VARIABLE}}")
			set(GCC_VERSION "${${GCC_VERSION_VARIABLE}}")
		endif()
	endif()

	search_cross_tool("${SEARCH_DIRECTORY}" "${GCC_NAME}" "${GCC_NAME_REGEX}"
		1 "-v" "${GCC_VERSION_STRING_REGEX}" "${GCC_TARGET_STRING_REGEX}" "${GCC_TARGET_REGEX}"
		GCC_PATH GCC_VERSION)

	if(DEFINED GCC_PATH)
		if(DEFINED GCC_VERSION)
			set(${GCC_PATH_VARIABLE} "${GCC_PATH}" PARENT_SCOPE)
			set(${GCC_VERSION_VARIABLE} "${GCC_VERSION}" PARENT_SCOPE)
		endif()
	endif()
endfunction()

function(search_cross_gas SEARCH_DIRECTORY GAS_TARGET_REGEX GAS_PATH_VARIABLE GAS_VERSION_VARIABLE)
	set(GAS_VERSION_STRING_REGEX "GNU assembler version ([0-9]+([.][0-9]+)+).*")
	set(GAS_VERSION_STRING_REGEX2 "GNU assembler \\(GNU Binutils.*\\) ([0-9]+([.][0-9]+)+).*")
	set(GAS_TARGET_STRING_REGEX ".*This assembler was configured for a target of `([A-Za-z0-9\\._]+([-][A-Za-z0-9\\._]+)+)'\\..*")
	if(DEFINED ${GAS_PATH_VARIABLE})
		if(DEFINED ${GAS_VERSION_VARIABLE})
			set(GAS_PATH "${${GAS_PATH_VARIABLE}}")
			set(GAS_VERSION "${${GAS_VERSION_VARIABLE}}")
		endif()
	endif()

	search_cross_tool("${SEARCH_DIRECTORY}" "as" "${GAS_NAME_REGEX}"
		0 "-version" "${GAS_VERSION_STRING_REGEX}" "${GAS_TARGET_STRING_REGEX}" "${GAS_TARGET_REGEX}"
		GAS_PATH GAS_VERSION)
	search_cross_tool("${SEARCH_DIRECTORY}" "as" "${GAS_NAME_REGEX}"
		0 "-version" "${GAS_VERSION_STRING_REGEX2}" "${GAS_TARGET_STRING_REGEX}" "${GAS_TARGET_REGEX}"
		GAS_PATH GAS_VERSION)

	if(DEFINED GAS_PATH)
		if(DEFINED GAS_VERSION)
			set(${GAS_PATH_VARIABLE} "${GAS_PATH}" PARENT_SCOPE)
			set(${GAS_VERSION_VARIABLE} "${GAS_VERSION}" PARENT_SCOPE)
		endif()
	endif()
endfunction()
